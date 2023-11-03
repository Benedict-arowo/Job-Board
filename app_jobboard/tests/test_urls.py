from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import index as auth_index, loginUser, registerUser, logoutUser
from app_jobboard.views_folder import *
class TestAuthUrls(SimpleTestCase):
    def test_auth_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, auth_index)

    def test_auth_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginUser)

    def test_auth_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerUser)

    def test_auth_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)


class TestJobboardUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, index)
    
    def test_createJob_url(self):
        url = reverse('createJob')
        self.assertEquals(resolve(url).func, createJob)

    def test_myjobs_url(self):
        url = reverse('myJobs')
        self.assertEquals(resolve(url).func, getUserJobs)

    def test_mycompanies_url(self):
        url = reverse('myCompanies')
        self.assertEquals(resolve(url).func, getUserCompanies)
    
    def test_company_url(self):
        url = reverse('company')
        self.assertEquals(resolve(url).func, companies)
    