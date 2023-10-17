from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Job, JobCategory
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required(login_url="auth:index")
@require_http_methods(["POST"])
def createJob(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    company_name = request.POST.get("company_name")
    location = request.POST.get("location")
    skills_required = request.POST.get("skills_required")
    application_deadline_date = request.POST["application_deadline_date"]
    application_deadline_time = request.POST.get("application_deadline_time")
    employment_type = request.POST.get("employment_type")
    salary = request.POST.get("salary")
    currency = request.POST.get("currency")
    apply_link = request.POST.get("apply_link")
    category = request.POST.get("category")

# TODO: Validations
    if not name:
        messages.error(request, "Please provide a name for this job posting.")
        return redirect()


    try:
        category, status = JobCategory.objects.get_or_create(name=category)
        job = Job.objects.create(
            category=category,
            employer=request.user,
            name=name,
            description=description,
            company_name=company_name,
            location=location,
            skills_required=skills_required,
            employment_type=employment_type,
            application_deadline=f"{application_deadline_date} {application_deadline_time}",
            is_active=True,
            salary=salary,
            currency=currency,
            apply_link=apply_link,
        )
        job.save()
    except:
        messages.error(request, "Error while trying to create your job posting.")
        return redirect("jobboard:index")

    return redirect("jobboard:index")
