from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from test_utils import create_user
from unittest.mock import patch


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
            get_user_model().objects.create_user('', 'password123')

    def test_create_superuser_ok(self):
        user = get_user_model().objects.create_superuser('test@gmail.com', 'password123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample receipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient1'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    @patch('core.models.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')
