from django.urls import path
from . import views

app_name = "jobboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("job/<uuid:id>", views.getJob, name="job"),
    path("createJob/", views.createJob, name="createJob"),
    path("editJob/<uuid:id>", views.editJob, name="editJob"),
    path("deleteJob/<uuid:id>", views.deleteJob, name="deleteJob"),
]
