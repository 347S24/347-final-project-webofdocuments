from django.urls import path
from . import views
from .views import document_detail_view

app_name="matrix"
urlpatterns = [
    path('~editor/', views.editor, name='editor'),
    path('document/<int:pk>', view=document_detail_view, name='document_detail')
]