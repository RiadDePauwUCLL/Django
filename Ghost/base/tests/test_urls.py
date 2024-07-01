from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *


class TestUrlsNotLoginRequired(SimpleTestCase):
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_room_url_resolves(self):
        url = reverse('room', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, room)

    def test_user_profile_url_resolves(self):
        url = reverse('user-profile', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, userProfile)

    def test_topics_url_resolves(self):
        url = reverse('topics')
        self.assertEquals(resolve(url).func, topicsPage)

    def test_activity_url_resolves(self):
        url = reverse('activity')
        self.assertEquals(resolve(url).func, activitiesPage)



class TestUrlsLoginRequired(SimpleTestCase):
    
    def setUp(self):
        pass

    def test_create_room_url_resolves(self):
        pass

    def test_update_room_url_resolves(self):
        pass

    def test_delete_room_url_resolves(self):
        pass

    def test_message_room_url_resolves(self):
        pass

    def test_update_user_url_resolves(self):
        pass