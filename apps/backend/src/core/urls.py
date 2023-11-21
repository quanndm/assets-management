from django.urls import path, include

urlpatterns = [
    path('', include('assets.urls')),
    path('', include('auth_app.urls')),
]
