from django.urls import path
from . import views
from .views import editor, document_detail_view

app_name = "matrix"
urlpatterns = [
    path('document/<int:pk>', view=document_detail_view, name='document_detail'),
    path('new_matrix/', views.editor, name='new_matrix'),
    path('new_node/', views.editor2, name='new_node'),
    # path('', views.blank_text_field, name='blank_text_field_page'),
    path('<str:document>/', view=editor),
    
]