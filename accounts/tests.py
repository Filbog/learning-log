from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


User = get_user_model()


# Create your tests here.
class RegistrationViewTests(TestCase):

    def test_registration_page_loads_correctly(self):
        response = self.client.get(reverse("accounts:register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_successful_registration(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "testuser",
                "password1": "testpaSS123word",
                "password2": "testpaSS123word",
                "email": "test@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)  # Adjust if you expect a redirect
        self.assertTrue(User.objects.filter(username="testuser").exists())

        user = User.objects.get(username="testuser")
        self.assertFalse(user.is_active)

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Activate your account.", mail.outbox[0].subject)

    def test_activation_link_activates_user(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com",
            is_active=False,
        )
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        activation_url = reverse(
            "accounts:activate", kwargs={"uidb64": uid, "token": token}
        )
        response = self.client.get(activation_url)

        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertTemplateUsed(
            response, "registration/email_confirmation_successful.html"
        )

    def test_invalid_activation_link(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com",
            is_active=False,
        )
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        invalid_token = "invalid-token"

        activation_url = reverse(
            "accounts:activate", kwargs={"uidb64": uid, "token": invalid_token}
        )
        response = self.client.get(activation_url)

        user.refresh_from_db()
        self.assertFalse(user.is_active)
        self.assertTemplateUsed(response, "registration/activation_link_invalid.html")
