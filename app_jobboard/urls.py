from django.urls import path
from . import views

app_name = 'jobboard'
urlpatterns = [path("", views.index, name="index")]
