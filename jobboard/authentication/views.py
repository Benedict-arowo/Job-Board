from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Authentication index page.")

def register_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')

# TODO: Check if username, password and role are valid, then check if the username isn't already taken, then register the user. 
    return 0