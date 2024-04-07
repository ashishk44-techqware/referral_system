from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, UserProfile, Referral
from rest_framework.test import APITestCase, APIClient

class UserRegistrationTestCase(APITestCase):
    def test_user_registration_success(self):
        url = reverse('register')
        data = {
            'name': 'Alok',
            'email': 'Alok@yopmail.com',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_with_referral_code(self):
        referring_user_profile = UserProfile.objects.create(user=User.objects.create(username='referral_user'))
        referring_user_profile.referral_code = '1C0VD5'
        referring_user_profile.save()

        url = reverse('register')
        data = {
            'name': 'Alok yadav',
            'email': 'Alokyadav@yopmail.com',
            'password': 'password123',
            'referral_code':'1C0VD5'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginUserTestCase(APITestCase):
    def test_login_user_success(self):

        user = User.objects.create_user(username='alok@yopmail.com', email='alok@yopmail.com', password='password123')
        
        url = reverse('login_user')
        data = {
            'email': 'alok@yopmail.com',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_invalid_credentials(self):
        url = reverse('login_user')
        data = {
            'email': 'notexist@yopmail.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserDetailsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alok@yopmail.com', email='alok@yopmail.com', password='password123')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user) 

    def test_user_details(self):
        url = reverse('user_profile')  # Adjust the reverse function call based on your URL pattern name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReferralsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alok@yopmail.com', email='alok@yopmail.com', password='password123')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_referrals(self):
        url = reverse('reffered_user_list')  # Assuming this is your URL pattern for the referrals view
        # self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

