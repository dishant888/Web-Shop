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
