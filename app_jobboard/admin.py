from django.contrib import admin
from .models import Job, JobApplication, CompanyCategory, Search, Bookmark, Company, CompanyReviews

# Register your models here.
Models = [Job, JobApplication, CompanyCategory, Search, Bookmark, Company, CompanyReviews]
# Registers the models in the models list.
for model in Models:
    admin.site.register(model)
