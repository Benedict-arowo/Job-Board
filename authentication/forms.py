from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password", "middle_name", "role"]