from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ToDoAuthorizationTest(APITestCase):
    def test_list_endpoint_response_status_is_asking_authorization(self):
        """ test if user is authorized to view the list of todos"""
        response = self.client.get(reverse('todo:list-create'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_admin_endpoint_response_status_is_asking_authorization(self):
        """ test if user is authorized to view the list as admin todos"""
        response = self.client.get(reverse('todo:list-admin'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_archived_endpoint_response_status_is_asking_authorization(self):
        """ test if user is authorized to view the list as admin todos"""
        response = self.client.get(reverse('todo:list-archived'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
