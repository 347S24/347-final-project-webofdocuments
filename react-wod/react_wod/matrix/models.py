from django.db import models
# from django.urls import reverse
from react_wod.users.models import User

"""Model represents a collection of files"""
class Matrix(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="enter the title of this matrix"
    )
    # main data that will be stored in a matrix (a group of files)
    
    owner = models.ForeignKey(User, models.CASCADE)
    
    # connections = ;

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Document(models.Model):
    file_name = models.CharField(
        max_length=200,
        help_text="enter the filename"
    )
    # FIXME
    file_contents = models.FileField(null=True,blank=True)
    # FIXME
    matrix = models.ForeignKey(Matrix, models.CASCADE, related_name='documents', null=True,blank=True)

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
