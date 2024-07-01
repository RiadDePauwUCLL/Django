from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *


class TestUrlsNotLoginRequired(SimpleTestCase):
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_resolves(self):
        url = reverse('')

    def test_home_url_resolves(self):
        url = reverse('')

    def test_room_url_resolves(self):
        url = reverse('')

    def test_user_profile_url_resolves(self):
        url = reverse('')

    def test_topics_url_resolves(self):
        url = reverse('')

    def test_activity_url_resolves(self):
        url = reverse('')



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