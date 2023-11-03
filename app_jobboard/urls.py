from django.urls import path
from . import views
from .views_folder import company_views, company_reviews

app_name = "jobboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("job/<uuid:id>", views.getJob, name="job"),
    path("createJob/", views.createJob, name="createJob"),
    path("myJobs/", views.getUserJobs, name="getUserJobs"),
    path("company/", views.companies, name="companies"),
    path("editJob/<uuid:id>", views.editJob, name="editJob"),
    path("deleteJob/<uuid:id>", views.deleteJob, name="deleteJob"),
    path("deleteSearch/<int:id>", views.deleteSearch, name="deleteSearch"),
    path("bookmark/<uuid:jobId>", views.addJobToBookmark, name="addBookmark"),
    path(
        "remove_bookmark/<uuid:jobId>",
        views.removeJobFromBookmark,
        name="removeBookmark",
    ),
    
    path("company/<uuid:id>/", company_views.company, name="company"),
    path("company/create/", company_views.createCompany, name="createCompany"),
    path("company/edit/<uuid:id>/", company_views.editCompany, name="editCompany"),
    path("company/delete/<uuid:id>/", company_views.deleteCompany, name="deleteCompany"),
    path("companies/", company_views.userCompanies, name="userCompanies"),
]

# TODO: Organize URLS into separate files.
# TODO: Change bookmark, and remove bookmark view to only retun json response
