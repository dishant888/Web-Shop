from django.urls import path
from items.api.views import ItemAPI

urlpatterns = [
    path('add/', ItemAPI.as_view())
]
