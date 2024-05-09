from django import forms
from .models import Matrix, Document

class MatrixForm(forms.ModelForm):
    class Meta:
        model = Matrix
        fields = ['title']

class NodeForm(forms.ModelForm):
    # text_field = forms.CharField(label='Write info here')
    class Meta:
        model = Document
        fields = ['file_name', 'file_contents', 'matrix']
        # https://stackoverflow.com/questions/66707030/django-textarea-form
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20, 'cols': 80})
        }