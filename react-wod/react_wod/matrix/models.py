from django.db import models
# from django.urls import reverse
from users.models import User

"""Model represents a collection of files"""
class Matrix(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="enter the title of this matrix"
    )
    # main data that will be stored in a matrix (a group of files)
    documents = models.FileField()
    owner = models.ForeignKey(User)
    
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
    # file_contents = ;
    # FIXME
    # matrix = ;

    def __str__(self):
        """String for representing the Model object."""
        return self.file_name
    
# class Connection(models.Model):
#     # start_node = ;
#     # end_node = ;
#     # matrix = ;