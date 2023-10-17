from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import index, loginUser, registerUser, logoutUser

class TestAuthUrls(SimpleTestCase):
    def test_auth_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

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
    pass
