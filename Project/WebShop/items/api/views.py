from rest_framework.views import APIView
from items.api.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ItemAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def post(self, req):
        item = ItemSerializer(context = {'user_id': req.user.id}, data = req.data)

        if item.is_valid():
            item.save()
            return Response(item.data, status = status.HTTP_201_CREATED)
        
        return Response(item.errors, status = status.HTTP_400_BAD_REQUEST)