from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    username = serializers.CharField(max_length = 150, required = True)
    # email kept as CharField and not EmailField (it will not check the email for regular expression)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only = True)

    # check for unique username and email
    def validate(self, attrs):

        if User.objects.filter(username = attrs['username']).exists(): 
            raise serializers.ValidationError({'username': ['This username is already in use.']})
        
        if User.objects.filter(email = attrs['email']).exists(): 
            raise serializers.ValidationError({'email': ['This email is already in use.']})
            
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):

    current_password = serializers.CharField(required = True, write_only = True)
    new_password = serializers.CharField(required = True, write_only = True)

    def validate(self, attrs):

        user = self.context['user']

        if not user.check_password(attrs['current_password']):
            raise serializers.ValidationError({"current_password": ["Current password is incorrect."]})
        
        if attrs['current_password'] == attrs['new_password']:
            raise serializers.ValidationError({"new_password": ["Current password and new password cannot be same."]})

        return super().validate(attrs)
    
    def update(self, instance, validated_data):

        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance