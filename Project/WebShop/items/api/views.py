from rest_framework.generics import GenericAPIView
from items.api.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from items.models import Item
from items.api.paginators import ItemPaginator
from django.shortcuts import get_object_or_404

# Functional requirement 7 (Add item)
# API to create new item (authentication required)
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
# API to get all the items (no authentication required)
class ListItemsAPI(GenericAPIView):

    pagination_class = ItemPaginator

    def get(self, req):

        items = Item.objects.filter(on_sale = True).order_by('-date', '-id')
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
        try:
            filter_by = req.query_params['filter_by']

            if filter_by == 'sale':items = Item.objects.filter(seller_id = req.user.id).filter(on_sale = True)
            if filter_by == 'sold': items = Item.objects.filter(seller_id = req.user.id).filter(on_sale = False)
            if filter_by == 'purchased': items = Item.objects.filter(buyer_id = req.user.id) 

            serializer = ItemSerializer(items, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        except Exception:
            return Response({'filter_by': ['filter_by query parameter is required.']}, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 4 (Search)
# API to search items by title
class SearchItemAPI(GenericAPIView):

    pagination_class = ItemPaginator

    def get(self, req):
        
        try:
            search_keyword = req.query_params['title']
            items = Item.objects.filter(title__startswith = search_keyword).filter(on_sale = True)
            page = self.paginate_queryset(items)

            if page:
                serializer = ItemSerializer(page, many=True)
                response = self.get_paginated_response(serializer.data)
                return Response(response.data, status = status.HTTP_200_OK)
            else:
                return Response({'results': []}, status = status.HTTP_200_OK)

        except Exception:
            return Response({'title': ['title query parameter is required.']}, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 14 (Edit Item)
# API for partial updates to item
class EditItemAPI(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, req, item_id):

        item =  get_object_or_404(Item, id = item_id)
        
        if item.seller.id != req.user.id: return Response({'item': ['You can only edit the items added by you.']}, status = status.HTTP_400_BAD_REQUEST)

        if not item.on_sale: return Response({'item': ['You can only edit the items which are currently on sale.']}, status = status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(instance = item, data = req.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)