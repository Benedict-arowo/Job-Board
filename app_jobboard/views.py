from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Job, Search, Bookmark, Company, CompanyReviews
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from custom_decorators import employer_only
from django.db.models import Q
from .forms import JobForm
from django.urls import reverse

# Create your views here.
def index(request):
    id = request.GET.get('job')
    q = request.GET.get('q')
    tab = request.GET.get('tab')
    context = {  }

    if q:
        q = q.lower()
        context["q"] = q.capitalize()
        # search = Search.objects.get_or_create(search=q.lower(), user=request.user)
        try:
            search = Search.objects.get(user=request.user, search=q)
            search.count += 1
            search.save()
        except Search.DoesNotExist:
            search = Search.objects.create(user=request.user, search=q)

        jobs = Job.objects.filter(Q(name__icontains=q) | Q(employment_type__icontains=q) | Q(location__icontains=q)).order_by('-updated_at', '-created_at')
    else:
        jobs = Job.objects.all().order_by('-updated_at', '-created_at')

    if id:
        job = Job.objects.get(id=id)
        context["job"] = job

        try:
            bookmarked = Bookmark.objects.get(job=job, user=request.user)
            if bookmarked:
                context["bookmarked"] = True
        except:
            pass

    context["jobs"] = jobs

    if tab == "recent_searches":
        if request.user.is_authenticated:
            context["recent_searches"] = Search.objects.filter(user=request.user).order_by("-updated", "-created")
            context["tab"] = tab

    return render(request, "index.html", context)

def getJob(request, id):
    job = Job.objects.get(id=id)
    context = { "job": job }
    return render(request, "jobboard/job.html", context)

@login_required(login_url="auth:index")
def getUserJobs(request):
    q = request.GET.get('q')
    context = {}
    if q:
        context['q'] = q
        context['jobs'] = Job.objects.filter(Q(employer=request.user) & (Q(name__icontains=q) | Q(location__icontains=q) | Q(employment_type__icontains=q))).order_by('-updated_at', '-created_at')
    else:
        context['jobs'] = Job.objects.filter(employer=request.user).order_by('-updated_at', 'created_at')

    return render(request, "jobboard/manageJobs.html", context)


@login_required(login_url="auth:index")
def getUserCompanies(request):
    userCompanies = Company.objects.filter(owner=request.user)
    context = {
        "companies": userCompanies
    }
    return render(request, "jobboard/manageCompanies.html", context)

@login_required(login_url="auth:index")
@employer_only
def createJob(request):
    form = JobForm()
    if request.method == "POST":
        jobForm = JobForm(request.POST)
        if not jobForm.is_valid():
            print(jobForm.errors)
        if jobForm.is_valid():
            form = jobForm.save(commit=False)
            form.employer = request.user
            form.save()
            print(form.id)
            return redirect("jobboard:job", id=form.id)
            # return redirect(reverse("jobboard:index") + f"?job={form.id}")
    context = {"form": form}
    return render(request, "jobboard/createJob.html", context)


@login_required(login_url="auth:index")
@employer_only
def editJob(request, id):
    jobInstance = Job.objects.get(id=id)
    form = JobForm(instance= jobInstance)

    if request.method == "POST":
        jobForm = JobForm(request.POST, instance=jobInstance)

        if not jobForm.is_valid():
            print(jobForm.errors)

        if jobForm.is_valid():
            form = jobForm.save(commit=False)
            form.employer = request.user
            form.save()
            return redirect('jobboard:job', id=form.id)

    context = {"form": form, "id": id}
    return render(request, "jobboard/editJob.html", context)


@login_required(login_url="auth:index")
@employer_only
def deleteJob(request, id):
    try:
        job = Job.objects.get(id=id)
    except:
        messages.error(request, "Job with the id provided was not found.")
        return redirect("jobboard:index")

    if job.employer != request.user:
        messages.error(request, "You do not have the permission to delete this job.")
        return redirect("jobboard:index")
    job.delete()

    next = request.GET.get('next', '/')
    if next:
        return HttpResponseRedirect(next)
    return redirect("jobboard:index")

@login_required(login_url="auth:index")
def addJobToBookmark(request, jobId):
    try: 
        job = Job.objects.get(id=jobId)
        Bookmark.objects.create(user=request.user, job=job)
    except Job.DoesNotExist:
        messages.error(request, "Job does not exist.")

    return redirect("jobboard:index")


@login_required(login_url="auth:index")
def removeJobFromBookmark(request, jobId):
    try: 
        job = Job.objects.get(id=jobId)
        Bookmark.objects.delete(user=request.user, job=job)
    except Job.DoesNotExist:
        messages.error(request, "Job does not exist.")

    return redirect("jobboard:index")

@login_required(login_url="auth:index")
def deleteSearch(request, id):
    try:
        search = Search.objects.get(id=id)
        if search.user == request.user:
            search.delete()
        else:
            raise "You do not have permission to delete this search entry."
    except:
        messages.error(request, "Error trying to delete search entry.")

    return redirect(reverse("jobboard:index") + "?tab=recent_searches")

def companies(request):
    q = request.GET.get('q')
    tab = request.GET.get('tab')
    context = { }

    if q:
        context['q'] = q
        context['companies'] = Company.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q))
    else:
     context['companies']= Company.objects.all()

    if tab:
        context['tab'] = tab
        
    return render(request, "jobboard/companies.html", context)

def company(request, id):
    company = Company.objects.get(id=id)
    reviews = CompanyReviews.objects.filter(company=company)
        
    context = {
        "company": company,
        "reviews": reviews
    }
    return render(request, "jobboard/company.html", context)
