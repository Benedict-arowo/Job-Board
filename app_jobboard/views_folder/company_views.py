from app_jobboard.models import Company, CompanyReviews, Job
from django.shortcuts import render, redirect
from ..forms import CompanyForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def company(request, id):
    company = Company.objects.get(id=id)
    reviews = CompanyReviews.objects.filter(company=company)
    jobs = Job.objects.filter(company=company)

    context = {"company": company, "reviews": reviews, "jobs": jobs}
    return render(request, "jobboard/company.html", context)


@login_required(login_url="auth:index")
def createCompany(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect("jobboard:company", id=form.id)
        else:
            messages.error(request, "Error trying to create company.")
            return redirect("jobboard:createCompany")

    context = {"form": CompanyForm}
    return render(request, "company/create.html", context)


@login_required(login_url="auth:index")
def editCompany(request, id):
    print(id)
    try:
        company = Company.objects.get(id=id)
        if request.method == "POST":
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                form = form.save()
                return redirect("jobboard:company", id=form.id)

        context = {
            "form": CompanyForm(instance=company),
            "mode": "edit",
            "company": company,
        }

        return render(request, "company/create.html", context)
    except Company.DoesNotExist:
        messages.error(request, "Error trying to find company.")
        return redirect("jobboard:index")
        # TODO: redirect back to the page they came from.


@login_required(login_url="auth:index")
def deleteCompany(request, id):
    try:
        company = Company.objects.get(id=id)

        if company.owner != request.user:
            messages.error(request, "You do not have permission to delete this company")
            return redirect("jobboard:index")

        company.delete()
        return redirect("jobboard:userCompanies")

    except Company.DoesNotExist:
        messages.error(request, "Error trying to find company.")
        return redirect("jobboard:index")


@login_required(login_url="auth:index")
def userCompanies(request):
    q = request.GET.get("q")
    context = {}

    if q:
        context["q"] = q
        context["companies"] = Company.objects.filter(
            Q(owner=request.user) & Q(name__icontains=q)
            | Q(description__icontains=q)
            | Q(category__name__icontains=q)
        )
    else:
        context["companies"] = Company.objects.filter(owner=request.user)

    return render(request, "jobboard/manageCompanies.html", context)
