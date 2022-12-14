from rest_framework.generics import GenericAPIView
from items.api.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from items.models import Item
from items.api.paginators import ItemPaginator
from rest_framework.filters import SearchFilter

# Functional requirement 7 (Add item)
# API to create card (authentication required)
class CreateItemAPI(GenericAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def post(self, req):

        item = ItemSerializer(context = {'user_id': req.user.id}, data = req.data)

        if item.is_valid():
            item.save()
            return Response(item.data, status = status.HTTP_201_CREATED)
        
        return Response(item.errors, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 3 (Browse)
# API to read all the cards (no authentication required)
class ListItemsAPI(GenericAPIView):

    # todo list of items on 'sale' not all

    pagination_class = ItemPaginator

    def get(self, req):

        items = Item.objects.order_by('-date')
        page = self.paginate_queryset(items)

        if page:
            serializer = ItemSerializer(page, many = True)
            response = self.get_paginated_response(serializer.data)
            return Response(response.data, status = status.HTTP_200_OK)
        else:
            return Response([], status = status.HTTP_404_NOT_FOUND)

# Functional requirement 13 (Display inventory)
# API to get all the items (sale, sold, and brought) of the authenticated user
class ListInventoryAPI(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, req):
        items = Item.objects.filter(added_by = req.user.id)
        response = ItemSerializer(items, many = True)
        return Response(response.data, status = status.HTTP_200_OK)

# Functional requirement 4 (Search)
# API to search items by title
class SearchItemAPI(GenericAPIView):

    # todo search items on 'sale' not all

    pagination_class = ItemPaginator

    def get(self, req):
        search_keyword = req.query_params['title']

        if search_keyword:
            items = Item.objects.filter(title__startswith = search_keyword)
            page = self.paginate_queryset(items)

            if page:
                serializer = ItemSerializer(page, many=True)
                response = self.get_paginated_response(serializer.data)
                return Response(response.data, status = status.HTTP_200_OK)
            else:
                return Response([], status = status.HTTP_404_NOT_FOUND)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)