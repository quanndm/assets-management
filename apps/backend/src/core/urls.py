from django.urls import path, include
from rest_framework import permissions

urlpatterns = [
    path('', include('assets.urls')),
]