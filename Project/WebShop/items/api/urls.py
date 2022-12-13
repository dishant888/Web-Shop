from django.urls import path
from items.api.views import CreateItemAPI, ListItemsAPI, ListInventoryAPI

urlpatterns = [
    path('', ListItemsAPI.as_view()),
    path('add/', CreateItemAPI.as_view()),
    path('inventory/', ListInventoryAPI.as_view()),
]
