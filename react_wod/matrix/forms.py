from django import forms
from .models import Matrix, Document

class MatrixForm(forms.ModelForm):
    class Meta:
        model = Matrix
        fields = ['title']
    

class NodeForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file_name', 'file_contents', 'matrix']