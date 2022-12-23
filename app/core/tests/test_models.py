from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_ok(self):
        email = 'asd@gmail.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_with_email_normalized(self):
        emails = [
            ['asd1@GMAIL.com', 'asd1@gmail.com'],
            ['ASD2@gmail.com', 'ASD2@gmail.com'],
            ['ASD3@GMAIL.com', 'ASD3@gmail.com'],
            ['ASD4@gmail.COM', 'ASD4@gmail.com'],
            ['ASD5@GMAIL.COM', 'ASD5@gmail.com'],
        ]

        for email, expected in emails:
            user = get_user_model().objects.create_user(email, 'password123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('email', 'password123')
