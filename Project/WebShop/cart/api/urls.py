from django.urls import path
from cart.api.views import AddToCartAPI, ListCartItemsAPI, DeleteCartItem, BuyCartItemsAPI

urlpatterns = [
    path('', ListCartItemsAPI.as_view()),
    path('add/<int:item_id>', AddToCartAPI.as_view()),
    path('delete/<int:item_id>', DeleteCartItem.as_view()),
    path('buy/', BuyCartItemsAPI.as_view()),
]
