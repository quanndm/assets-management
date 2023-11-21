from django.urls import path, include
from .views import (
    token,
    user_profile,
    change_password
)

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', user_profile.UserProfileViewSet,
                basename="profile")

urlpatterns = [
    path('login/', token.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot_password/', user_profile.forgot_pwd, name='forgot_pwd'),
    path('change_password/',
         change_password.ChangePasswordView.as_view(), name='auth_change_password'),
    path("", include(router.urls)),
]
