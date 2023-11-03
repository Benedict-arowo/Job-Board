from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import index as authIndex, loginUser, registerUser, logoutUser
from app_jobboard.views import index, createJob, getUserJobs, companies
from app_jobboard.views_folder import company_views
class TestAuthUrls(SimpleTestCase):
    def test_auth_index_url(self):
        url = reverse('auth:index')
        self.assertEqual(resolve(url).func, authIndex)

    def test_auth_login_url(self):
        url = reverse('auth:login')
        self.assertEqual(resolve(url).func, loginUser)

    def test_auth_register_url(self):
        url = reverse('auth:register')
        self.assertEqual(resolve(url).func, registerUser)

    def test_auth_logout_url(self):
        url = reverse('auth:logout')
        self.assertEqual(resolve(url).func, logoutUser)


class TestJobboardUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('jobboard:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_createJob_url(self):
        url = reverse('jobboard:createJob')
        self.assertEqual(resolve(url).func, createJob)

    def test_myjobs_url(self):
        url = reverse('jobboard:getUserJobs')
        self.assertEqual(resolve(url).func, getUserJobs)

    def test_mycompanies_url(self):
        url = reverse('jobboard:userCompanies')
        self.assertEqual(resolve(url).func, company_views.userCompanies)
    
    def test_company_url(self):
        url = reverse('jobboard:companies')
        self.assertEqual(resolve(url).func, companies)
    