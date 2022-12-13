from django.urls import path
from accounts.api.views import UserAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserAPI.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
