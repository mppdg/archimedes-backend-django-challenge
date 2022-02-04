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
        response = client.get(reverse('get_post_users'))
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        self.assertEqual(response.data.get('users'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateUserTest(TestCase):
    """ Test module for creating a user """

    def setUp(self):
        self.valid_payload = {
                'user': {
                'name': 'Tester Four',
                'email': 'four@tester.com',
                'role': 'User'
            }
        }
        self.invalid_payload = {
                'user': {
                'name': '',
                'email': 'four@tester.com',
                'role': 'Newrole',
            }
        }

    def test_create_valid_user(self):
        response = client.post(reverse('get_post_users'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(reverse('get_post_users'), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleUserTest(TestCase):
    """ Test module for updating an existing user profile """

    def setUp(self):
        self.tester_one = Profile.objects.create(name='Tester One', email="one@tester.com", role='User')
        self.tester_two = Profile.objects.create(name='Tester Two', email="two@tester.com", role='Admin')

        self.valid_payload = {
            'user': {
                'name': 'Updated Name',
                'role': 'Admin'
            }
        }

        self.invalid_payload = {
            'user': {
                'name': '',
                'role': 'Newrole',
            }
        }

    def test_valid_update_user(self):
        response = client.put(reverse('update_delete_user', kwargs={'user_id': self.tester_one.pk}),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_user(self):
        response = client.put(reverse('update_delete_user', kwargs={'user_id': self.tester_two.pk}),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleUserTest(TestCase):
    """ Test module for deleting a user profile """

    def setUp(self):
        self.tester_five = Profile.objects.create(name='Tester Five', email="five@tester.com", role='User')
        self.tester_six = Profile.objects.create(name='Tester Six', email="six@tester.com", role='Admin')

    def test_valid_delete_user(self):
        response = client.delete(reverse('update_delete_user', kwargs={'user_id': self.tester_five.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_user(self):
        response = client.delete(
            reverse('update_delete_user', kwargs={'user_id': 470}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)