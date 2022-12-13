from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 150, required = True)
    # email kept as CharField and not EmailField (it will not check the email for regular expression)
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)

    # check for unique username and email
    def validate(self, attrs):

        if User.objects.filter(username = attrs['username']).exists(): 
            raise serializers.ValidationError({'username': 'This username is already in use'})
        
        if User.objects.filter(email = attrs['email']).exists(): 
            raise serializers.ValidationError({'email': 'This email is already in use'})
            
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:

        model = User
        fields = ['username', 'email', 'password']
