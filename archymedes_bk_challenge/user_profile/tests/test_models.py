from django.test import TestCase
from ..models import Profile


class ProfileTest(TestCase):
    """ Test module for Profile model """
    
    def setUp(self):
        Profile.objects.create(
            name='Tester One', email="one@tester.com", role='User')
        Profile.objects.create(
            name='Tester Two', email="two@tester.com", role='Admin')

    def test_profile_entry(self):
        tester_one = Profile.objects.get(email='one@tester.com')
        tester_two = Profile.objects.get(email='two@tester.com')
        self.assertEqual(tester_one.name, "Tester One")
        self.assertEqual(tester_one.role, "User")
        self.assertEqual(tester_two.name, "Tester Two")
        self.assertEqual(tester_two.role, "Admin")