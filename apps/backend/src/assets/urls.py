from django.urls import include, path
from rest_framework import routers
from .views.CategoryViewSets import CategoryViewSet

router = routers.DefaultRouter()
router.register(r"api/categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
