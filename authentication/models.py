from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    profile_picture = models.FileField(upload_to="profile-pictures/", null=True)
    verified_email = models.BooleanField(default=False)
    phone_number = models.IntegerField(blank=True, null=True)
    country = models.CharField(blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "middle_name",
        "last_name",
        "username"
    ]

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

