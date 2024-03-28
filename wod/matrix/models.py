from django.db import models
# from django.urls import reverse

"""Model represents a collection of files"""
class Matrix(models.Model):
    # main data that will be stored in a matrix (a group of files)
    documents = models.FileField()
    
    