from django.db import models
from django.urls import reverse
from django.conf import settings
from react_wod.users.models import User
from django.contrib.auth import get_user_model


def get_default_user():
    """Helper function to get the default user id."""
    User = get_user_model()
    admin_user = User.objects.filter(is_superuser=True).first()
    if admin_user:
        return admin_user.id
    else:
        raise ValueError("No superuser exists; inable to assign a document owner.")


"""Model represents a collection of files"""
class Matrix(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="enter the title of this matrix"
    )
    # main data that will be stored in a matrix (a group of files)
    
    owner = models.ForeignKey(User, models.CASCADE, related_name='owned_matricies')
    
    # connections = ;

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Document(models.Model):
    file_name = models.CharField(
        max_length=200,
        help_text="Enter the filename"
    )
    # changed from filefield to textfield to store directly in db
    file_contents = models.TextField(blank=True, help_text="Markdown content of the file goes here")

    matrix = models.ForeignKey(Matrix, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)

    # refer to User model indirectly via auth_user_model
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_documents', 
                              default=get_default_user)

    def get_absolute_url(self):
        """Return absolute URL to the document.""" 
        return reverse("document_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.file_name
    

class Connection(models.Model):
    start_node = models.ForeignKey(Document, models.CASCADE, related_name='departures')
    end_node = models.ForeignKey(Document, models.CASCADE, related_name='arrivals')
    matrix = models.ForeignKey(Matrix, models.CASCADE, related_name='connections')

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.start_node} ==> {self.end_node}"
