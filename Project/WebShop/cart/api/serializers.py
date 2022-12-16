from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'item_id', 'title', 'price']