import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Profile
from ..serializers import ProfileSerializer

client = Client()

class GetAllUsersTest(TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        Profile.objects.create(name='Tester One', email="one@tester.com", role='User')
        Profile.objects.create(name='Tester Two', email="two@tester.com", role='Admin')

    def test_get_all_user_profiles(self):
        response = client.get('/api/v1/users/')
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        self.assertEqual(response.data.get('users'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)