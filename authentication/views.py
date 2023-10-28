from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from custom_decorators import guest_only
from password_strength import PasswordPolicy
from validate_email_address import validate_email
from django.urls import reverse

policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
)


@guest_only
def index(request):
    # TODO: Have the index page manage both the login and register template using JavaScript, so both loginUser, and registerUser view would only allow POST methods.
    mode = request.GET.get("mode")
    if not mode:
        mode = "login"
    roles = [
        {"value": "EMPLOYER", "display_value": "Employer"},
        {"value": "JOB SEEKER", "display_value": "Job Seeker"},
    ]

    return render(
        request, "authentication/auth.html", context={"mode": mode, "roles": roles}
    )


@guest_only
@require_http_methods(["POST"])
def loginUser(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    # Checks if an email address has been provided.
    if not email:
        messages.error(request, "Please enter an email address")
        return redirect("auth:index")

    # Checks if a password has been provided.
    if not password:
        messages.error(request, "Please enter a password.")
        return redirect("auth:index")

    # Tries to authenticate user, and if successful, it logs in the user.
    User = authenticate(request=request, email=email.lower(), password=password)
    if User is not None:
        login(request, User)
        return redirect("jobboard:index")
    else:
        messages.error(request, "Invalid username or password has been provided")
        return redirect("auth:index")


@guest_only
@require_http_methods(["POST"])
def registerUser(request):
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")
    role = request.POST.get("role")
    password = request.POST.get("password")

    # TODO: Better validation for passwords, and for roles.

    if not first_name or not last_name:
        messages.error(request, "You must provide a first name, and a last name.")
        return redirect(reverse("auth:index") + "?mode=register")

    if not email or not password:
        messages.error(request, "You must provide a password, and an email address.")
        return redirect("auth:index")

    print(validate_email(email))
    if not validate_email(email):
        messages.error(request, "The email address provided is not valid.")
        return redirect("auth:index")

    if not len(policy.test(password)) == 0:
        messages.error(request, "The password provided is not strong enough.")
        return redirect("auth:index")

    if not role:
        messages.error(request, "You must provide a role.")
        return redirect("auth:index")

    try:
        User = CustomUser.objects.create(
            email=email.lower(),
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            role=role,
        )
        User.save()
        login(request=request, user=User)
        return redirect("jobboard:index")
    except:
        messages.error(request, "Error trying to create your account.")
        return redirect("auth:index")


@login_required(login_url="/auth")
def logoutUser(request):
    logout(request)
    return redirect("auth:index")


def user(request):
    context = {}
    return render(request, "authentication/user.html", context)


def editUser(request):
    context = {}
    return render(request, "authentication/user.html", context)
