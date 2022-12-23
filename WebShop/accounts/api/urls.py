from django.urls import path
from accounts.api.views import UserAPI, ChangePasswordAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserAPI.as_view()),
    # Functional requirement 6 (Login)
    path('login/', TokenObtainPairView.as_view()),
    path('change-password/', ChangePasswordAPI.as_view()),
]
