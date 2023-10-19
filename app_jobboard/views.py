from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Job, JobCategory, Search, Bookmark
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from custom_decorators import employer_only
from django.db.models import Q
from .forms import JobForm


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

        jobs = Job.objects.filter(Q(name__icontains=q) | Q(employment_type__icontains=q) | Q(location__icontains=q))
    else:
        jobs = Job.objects.all()

    if id:
        job = Job.objects.get(id=id)
        context["job"] = job

        bookmarked = Bookmark.objects.get(job=job, user=request.user)

        if bookmarked is not None:
            context["bookmarked"] = True

    context["jobs"] = jobs

    if tab == "recent_searches":
        context["recent_searches"] = Search.objects.filter(user=request.user).order_by("-updated", "-created")
        context["tab"] = tab

    return render(request, "index.html", context)

def getJob(request, id):
    job = Job.objects.get(id=id)
    context = { "job": job }
    return render(request, "jobboard/job.html", context)


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