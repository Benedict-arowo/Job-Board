from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from custom_decorators import guest_only

def index(request):
    # To make sure the user is not logged in already
    if request.user.is_authenticated:
        return redirect("jobboard:home")
    # TODO: Have the index page manage both the login and register template using JavaScript, so both loginUser, and registerUser view would only allow POST methods.
    return render(request, "authentication/login.html")


@require_http_methods(["POST"])
def loginUser(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    # Checks if an email address has been provided.
    if not email:
        messages.error(request, "Please enter an email address")
        return redirect("/auth")
    # Checks if a password has been provided.
    if not password:
        messages.error(request, "Please enter a password.")
        return redirect("/auth")

    # Tries to authenticate user, and if successful, it logs in the user.
    User = authenticate(request=request, email=email.lower(), password=password)
    if User is not None:
        login(request, User)
        return redirect("jobboard:home")
    else:
        messages.error(request, "Invalid username or password has been provided")
        return redirect("/auth")

@guest_only
def registerUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        role = request.POST.get("role")
        password = request.POST.get("password")

        # TODO: Better validation for passwords, and for roles.

        if not first_name or not last_name:
            messages.error(request, "You must provide a first name, and a last name.")
            return redirect("register")
        if not email or not password:
            messages.error(
                request, "You must provide a password, and an email address."
            )
            return redirect("register")
        if not role:
            messages.error(request, "You must provide a role.")
            return redirect("register")

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
            return redirect("home")
        except:
            messages.error(request, "Error trying to create your account.")
            return redirect("register")

    return render(request, "authentication/register.html")


@login_required(login_url="/auth")
def logoutUser(request):
    logout(request)
    return redirect("index")
