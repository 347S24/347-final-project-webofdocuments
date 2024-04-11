from django.urls import path, include
from . import views

urlpatterns = [
    # adds all the auth paths
    path('accounts/', include('django.contrib.auth.urls')),
]