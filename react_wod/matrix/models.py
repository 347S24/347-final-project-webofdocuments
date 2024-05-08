from django.db import models
from django.urls import reverse
from react_wod.users.models import User

"""Model represents a collection of files"""
class Matrix(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="enter the title of this matrix"
    )
    # main data that will be stored in a matrix (a group of files)
    
    owner = models.ForeignKey(User, models.CASCADE, related_name='owned_matricies', default=1)

    class Meta:
        app_label = 'matrix'
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Document(models.Model):
    file_name = models.CharField(
        max_length=200,
        help_text="enter the filename"
    )
    file_contents = models.TextField(blank=True, help_text="Markdown content of the file goes here", default='')

    matrix = models.ForeignKey(Matrix, models.CASCADE, related_name='documents', null=True, blank=True)

    # default owner will be the first super user created
    owner = models.ForeignKey(User, models.CASCADE, related_name='owned_documents', default=1)

    def get_absolute_url(self):
        """Return absolute URL to the document."""
        return reverse("documet_detail", kwargs={"pk": self.pk})

    

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