from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_ok(self):
        email = "asd@gmail.com"
        password = "123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_with_email_normalized(self):
        emails = [
            ["asd@GMAIL.com", "asd@gmail.com"],
            ["ASD@gmail.com", "ASD@gmail.com"],
            ["ASD@GMAIL.com", "ASD@gmail.com"],
            ["ASD@gmail.COM", "ASD@gmail.com"],
            ["ASD@GMAIL.COM", "ASD@gmail.com"],
        ]

        for email, expected in emails:
            user = get_user_model().objects.create_user(email, "password123")
            self.assertEqual(user.email, expected)
