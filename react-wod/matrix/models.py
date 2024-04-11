from django.db import models

"""Model represents a collection of files"""
class Matrix(models.Model):
    # main data that will be stored in a matrix (a group of files)
    documents = models.CharField(max_length=100)


class Unit(models.Model):
    group = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    unit = models.FileField(upload_to='unit/')
    
    # Don't need to have but is helpful
    created = models.DateTimeField(auto_now_add=True)
