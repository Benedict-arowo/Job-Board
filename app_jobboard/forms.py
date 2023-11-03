from django import forms
from .models import Job, Company, CompanyReviews


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ["employer", "is_active"]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ["owner"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReviews
        fields = "__all__"
        exclude = ["reviewer", "company"]
