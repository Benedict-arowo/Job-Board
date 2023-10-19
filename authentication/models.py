from django.db import models
from django.contrib.auth.models import AbstractUser


EMPLOYMENT_ROLE_CHOICES = (
    ("EMPLOYER", "Employer"),
    ("JOB SEEKER", "Job Seeker"),
)


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=16, choices=EMPLOYMENT_ROLE_CHOICES)
    profile_picture = models.FileField(upload_to="profile-pictures/", null=True)
    verified_email = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "middle_name",
        "last_name",
        "role",
        "username"
    ]

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

