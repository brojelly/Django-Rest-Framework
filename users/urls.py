# users/urls.py

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import LogoutView
from .views import UserSignupView, UserDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # ✅ JWT 로그인 & 갱신
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

