from django.urls import path
from . import views

app_name = "auth"
urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name="user"),
    path("edituser/", views.editUser, name="editUser"),
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
]
