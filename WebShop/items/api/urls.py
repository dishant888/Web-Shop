from django.urls import path
from items.api.views import CreateItemAPI, ListItemsAPI, ListInventoryAPI, SearchItemAPI, EditItemAPI

urlpatterns = [
    path('', ListItemsAPI.as_view()),
    path('add/', CreateItemAPI.as_view()),
    path('inventory/', ListInventoryAPI.as_view()),
    path('search/', SearchItemAPI.as_view()),
    path('edit/<int:item_id>', EditItemAPI.as_view())
]
