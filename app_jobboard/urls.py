from django.urls import path
from . import views

app_name = "jobboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("job/<uuid:id>", views.getJob, name="job"),
    path("createJob/", views.createJob, name="createJob"),
    path("myJobs/", views.getUserJobs, name="getUserJobs"),
    path("myComapanies/", views.getUserCompanies, name="getUserCompanies"),
    path("editJob/<uuid:id>", views.editJob, name="editJob"),
    path("deleteJob/<uuid:id>", views.deleteJob, name="deleteJob"),
    path("deleteSearch/<int:id>", views.deleteSearch, name="deleteSearch"),
    path("bookmark/<uuid:jobId>", views.addJobToBookmark, name="addBookmark"),
    path("remove_bookmark/<uuid:jobId>", views.removeJobFromBookmark, name="removeBookmark"),
]

# TODO: Change bookmark, and remove bookmark view to only retun json response