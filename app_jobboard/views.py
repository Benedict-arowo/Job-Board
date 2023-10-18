from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Job, JobCategory
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from custom_decorators import employer_only
from .forms import JobForm


# Create your views here.
def index(request):
    id = request.GET.get('job')
    print(id)
    if not id:
        job = None
    else:
        job = Job.objects.get(id=id)

    context = { "jobs": Job.objects.all(), "job": job }
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
