from items.models import Item
from rest_framework import serializers
from django.contrib.auth.models import User

class ItemSerializer(serializers.Serializer):

    title = serializers.CharField(required = True)
    description = serializers.CharField(required = True)
    price = serializers.FloatField(required = True)
    # user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())

    def create(self, validated_data):
        user = User.objects.get(id = self.context.get('user_id'))
        item = Item(title = validated_data['title'], description = validated_data['description'], price = validated_data['price'], added_by = user)
        item.save()
        return item

    class Meta:

        model = Item
        fields = ('__all__')