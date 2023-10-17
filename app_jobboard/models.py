import uuid
from django.db import models
from authentication.models import CustomUser


# Choices for employment types
EMPLOYMENT_TYPE_CHOICES = (
    ("Full-Time", "Full-Time"),
    ("Part-Time", "Part-Time"),
    ("Contract", "Contract"),
    ("Freelance", "Freelance"),
    ("Internship", "Internship"),
    ("Temporary", "Temporary"),
    ("Remote", "Remote"),
)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    skills_required = models.CharField(max_length=255)
    application_deadline = models.DateTimeField(blank=True, null=True)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    salary = models.IntegerField()
    currency = models.CharField(max_length=3, default="USD")
    apply_link = models.CharField(max_length=255)
    category = models.ForeignKey("JobCategory", on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} at {self.company_name} in {self.location}."

class JobSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ('Job Skills')

class JobApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Job Applications"


class JobCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Job Categories"

    def __str__(self):
        return self.name