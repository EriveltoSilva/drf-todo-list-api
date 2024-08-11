from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserAccountTest(APITestCase):
    def test_list_user_is_asking_authorization(self):
        resp = self.client.get(reverse('accounts:user-list'))
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_retrieve_user_is_asking_authorization(self):
    #     resp = self.client.get(reverse('accounts:user-retrieve-update-delete'))
    #     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileAccountAuthorizationTest(APITestCase):
    def test_list_profile_is_asking_authorization(self):
        resp = self.client.get(reverse('accounts:profile-list'))
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_retrieve_profile_is_asking_authorization(self):
    #     resp = self.client.get(reverse('accounts:profile-retrieve-update'))
    #     self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
