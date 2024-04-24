from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Matrix, Document

# Create your tests here.
class MatrixModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Setup data for the whole TestCase
        User = get_user_model()
        cls.superuser = User.objects.create_superuser(
            email='superuser@example.com',
            password='helloworld123'
        )
        print("Superuser created: ", cls.superuser.pk)
        cls.matrix = Matrix.objects.create(title='Test Matrix Simple', owner=cls.superuser)
        print("Matrix created: ", cls.matrix.pk)

    def test_title_label(self):
        matrix = Matrix.objects.get(pk=self.matrix.pk)
        field_label = matrix.matrix._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')