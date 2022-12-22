from rest_framework.generics import GenericAPIView
from accounts.api.serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from items.models import Item
import random
from django.shortcuts import redirect

# Functional requirement 5 (Create Account)
# API to create new user account
class UserAPI(GenericAPIView):

    def post(self, req):
    
        user = UserSerializer(data = req.data)

        if user.is_valid():
            user.save()
            return Response({"valid": True, "user": user.data}, status = status.HTTP_201_CREATED)
        
        return Response({"valid": False, "errors": user.errors}, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 12 (Edit Account)
# API to update password
class ChangePasswordAPI(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, req):
        user = req.user
        serializer = ChangePasswordSerializer(context = {'user': user}, data = req.data)

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response({'message': 'Password Updated'}, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 2 (Automatic DB population )
# API to pupulate data in the database
class PopulateDBAPI(GenericAPIView):
    
    def get(self, req):
        placeholder_titles = ['Sweater', 'Dress', 'Hoodies', 'T-shirt', 'Shorts', 'Socks', 'Jacket', 'Boots', 'Sunglasses', 'Hat', 'Jeans', 'Suit', 'Swimsuit', 'Long coat', 'Gloves']
        placeholder_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        # deleting all the user except the superuser
        User.objects.filter(is_superuser = False).delete()

        # creating new user and items
        item_no = 1
        for i in range(1,7):

            user_instance = User.objects.create_user(username = f'testuser{i}', email = f'testuser{i}@shop.aa', password = f'pass{i}')

            if i in range(1,4):
                user_data = UserSerializer(user_instance).data
                for j in range(1,11):
                    Item.objects.create(
                        title = random.choice(placeholder_titles), 
                        description = f'This is item number {j} added by {user_data["username"]}. {placeholder_text}', 
                        price = round(random.uniform(10,100),2), seller = user_instance
                        )
                    item_no += 1

        return redirect(req.META.get('HTTP_REFERER'))