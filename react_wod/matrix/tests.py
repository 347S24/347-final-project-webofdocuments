from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Matrix

class MatrixModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(
            username='admin',
            email='superuser@example.com',
            password='helloworld123'
        )
        cls.matrix = Matrix.objects.create(
            title='Test Matrix Simple',
            owner=cls.superuser  # Explicitly assigning the superuser
        )
        User = get_user_model()

    def test_title_label(self):
        matrix = Matrix.objects.get(pk=self.matrix.pk)
        field_label = matrix._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
