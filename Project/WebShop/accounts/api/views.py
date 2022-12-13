from rest_framework.views import APIView
from accounts.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class UserAPI(APIView):

    # saving a new user in the database
    def post(self, req):
    
        user = UserSerializer(data = req.data)

        if user.is_valid():
            user.save()
            return Response(user.data, status = status.HTTP_201_CREATED)
        
        return Response(user.errors, status = status.HTTP_400_BAD_REQUEST)
