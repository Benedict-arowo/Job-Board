from django.contrib import admin
from .models import Job, JobApplication, JobCategory

# Register your models here.
Models = [Job, JobApplication, JobCategory]
# Registers the models in the models list.
for model in Models:
    admin.site.register(model)
