from django.contrib import admin
from .models import Job, JobApplication, JobCategory, Search, Bookmark

# Register your models here.
Models = [Job, JobApplication, JobCategory, Search, Bookmark]
# Registers the models in the models list.
for model in Models:
    admin.site.register(model)
