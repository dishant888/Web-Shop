from items.models import Item
from rest_framework import serializers
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    
    price = serializers.FloatField(min_value = 0.1)

    class Meta:
        model = Item
        fields = ('__all__')

    def create(self, validated_data):
        user = User.objects.get(id = self.context.get('user_id'))
        item = Item(title = validated_data['title'], description = validated_data['description'], price = validated_data['price'], seller = user)
        item.save()
        return item