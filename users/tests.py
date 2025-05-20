from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "nickname": "tester",
            "password": "strongpass123"
        }
        self.user = User.objects.create_user(
            email="test@example.com", nickname="tester", password="strongpass123"
        )

    def test_user_signup(self):
        url = reverse("user-signup")
        data = {
            "email": "new@example.com",
            "nickname": "newbie",
            "password": "newpass123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        url = reverse("user-login")
        data = {"email": self.user.email, "password": "strongpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_login_invalid_credentials(self):
        url = reverse("user-login")
        data = {"email": self.user.email, "password": "wrongpass"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_get_user_details(self):
        self.client.login(email=self.user.email, password="strongpass123")
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user_details(self):
        self.client.login(email=self.user.email, password="strongpass123")
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {"nickname": "updated", "password": "updatedpass123"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        self.client.login(email=self.user.email, password="strongpass123")
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)