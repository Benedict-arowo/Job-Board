from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.contrib import messages
from ..forms import ReviewForm
from ..models import Company, CompanyReviews


# POST request only
@require_http_methods(["POST"])
def create_review(request, companyId):
    try:
        company = Company.objects.get(id=companyId)
    except company.DoesNotExist:
        messages.error(request, "Company provided does not exist.")
        return redirect("jobboard:index")

    form = ReviewForm(request.POST)
    if not form.is_valid():
        messages.error(request, form.errors)

    if form.is_valid():
        form = form.save(commit=False)
        form.reviewer = request.user
        form.company = company
        form.save()
        return redirect("jobboard:company", id=companyId)
    else:
        messages.error(request, "Error trying to create your review.")
        return redirect("jobboard:company", id=companyId)


@require_http_methods(["POST"])
def edit_review(request, id):
    try:
        review = CompanyReviews.objects.get(id=id)
    except review.DoesNotExist:
        messages.error(request, "Review does not exist.")
        return redirect("jobboard:index")

    form = ReviewForm(instance=review, data=request.POST)
    if form.is_valid():
        form = form.save()
        return redirect("jobboard:company", id=form.company.id)
    else:
        messages.error(request, "Error trying to edit review.")
        return redirect("jobboard:company", id=form.company.id)
