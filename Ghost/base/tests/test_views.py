from django.test import TestCase, Client
from django.urls import reverse, resolve
from base.models import User, Room, Topic
from django.contrib.auth import get_user



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test1',
            email='test@test.com',
            password='passwordisbig23'
        )

        self.topic = Topic.objects.create(name='Test Topic')

        self.room = Room.objects.create(
            host=self.user,
            topic=self.topic,
            name='Test Room',
            description='This is a test room'
        )


    ##                      TESTING GET ENDPOINTS


    def test_logoutUser_GET(self):
        self.client.login(email='test@test.com', password='passwordisbig23')

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_home_view_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_room_view_GET(self):
        response = self.client.get(reverse('room', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view_GET(self):
        response = self.client.get(reverse('user-profile', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_create_room_view_GET(self):
        response = self.client.get(reverse('create-room'))
        self.assertEqual(response.status_code, 302)

    def test_update_room_view_GET(self):
        response = self.client.get(reverse('update-room', args=['1']))
        self.assertEqual(response.status_code, 302)

    def test_delete_room_view_GET(self):
        response = self.client.get(reverse('delete-room', args=['1']))
        self.assertEqual(response.status_code, 302)

    def test_delete_message_view_GET(self):
        response = self.client.get(reverse('delete-message', args=['1']))
        self.assertEqual(response.status_code, 302)

    def test_update_user_view_GET(self):
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 302)

    def test_topics_page_view_GET(self):
        response = self.client.get(reverse('topics'))
        self.assertEqual(response.status_code, 200)

    def test_activities_page_view_GET(self):
        response = self.client.get(reverse('activity'))
        self.assertEqual(response.status_code, 200)





    ##                      TESTING POST ENDPOINTS


    def test_loginUser_POST(self):
        response = self.client.post(reverse('login'), {
            'email': 'test@test.com',
            'password': 'passwordisbig23'
        })

        self.assertEquals(response.status_code, 302)

        self.assertRedirects(response, reverse('home'))

        self.assertTrue(get_user(self.client).is_authenticated)