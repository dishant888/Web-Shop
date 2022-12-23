from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from cart.api.serializers import CartSerializer
from cart.models import Cart
from items.models import Item
from items.api.serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core import mail
from django.conf.global_settings import EMAIL_HOST_USER

def get_cart_items(user):

    cart_items = Cart.objects.filter(user = user)
    serializer = CartSerializer(cart_items, many = True)
    return serializer.data

# Functional requirement 8 (Add to cart)
# API to add items to cart
class AddToCartAPI(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, req, item_id):

        obj = get_object_or_404(Item, id = item_id)
        item = ItemSerializer(obj).data
        user = req.user
        
        if not item['on_sale']:
            return Response({'on_sale': ['This item is not on sale.']}, status = status.HTTP_400_BAD_REQUEST)
        
        if user.id == item['seller']:
            return Response({'seller': ['Cannot add your own item to the cart.']}, status = status.HTTP_400_BAD_REQUEST)
        
        if Cart.objects.filter(item_id = item_id).filter(user_id = user.id).exists():
            return Response({'seller': ['This item is already in the cart.']}, status = status.HTTP_400_BAD_REQUEST)

        cart_item = Cart(user = user, item = obj, title = item['title'], price = item['price'])
        cart_item.save()

        return Response(get_cart_items(req.user), status = status.HTTP_200_OK)

class ListCartItemsAPI(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, req):
        return Response(get_cart_items(req.user), status = status.HTTP_200_OK)

# Functional requirement 9 (Remove from cart)
# API to delete cart item
class DeleteCartItem(GenericAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, req, item_id):

        cart_item = Cart.objects.filter(item_id = item_id).filter(user_id = req.user.id)

        if cart_item.exists():
            cart_item.delete()
            return Response(get_cart_items(req.user), status = status.HTTP_200_OK)

        return Response({'buyer': ['This item is not in the cart.']}, status = status.HTTP_400_BAD_REQUEST)

# Functional requirement 10 (Pay)
# API to buy items in the cart of the logged in user
class BuyCartItemsAPI(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, req):

        user = req.user
        cart_items = get_cart_items(user)
        cart_item_ids = list()
        cart_ids = list()

        if len(cart_items) == 0:
            return Response({"cart": ['Your cart is empty, please add items to proceed.']}, status = status.HTTP_400_BAD_REQUEST)

        # checking if cart items are on sale and if price changed for any item in the cart
        for cart in cart_items:

            item = Item.objects.get(id = cart['item_id'])

            if item.price != cart['price']:
                # update new price
                serializer = CartSerializer(instance = Cart.objects.get(id = cart["id"]), data = {'price': item.price}, partial = True)
                serializer.is_valid(raise_exception = True)
                serializer.save()
                cart['old_price'] = cart['price']
                cart['price'] = item.price
                # send notification of change in price
                cart['notification'] = f'The price of {cart["title"]} has been updated from €{cart["old_price"]} to €{item.price}.'
                print(cart_items)
                return Response(cart_items, status = status.HTTP_406_NOT_ACCEPTABLE)

            if not item.on_sale:
                # send notification to remove item from cart as it is already sold
                cart['notification'] = f'{cart["title"]} is no longer avaliable for sale, please remove it from your cart.'
                return Response(cart_items, status = status.HTTP_406_NOT_ACCEPTABLE)
            
            cart_item_ids.append(cart['item_id'])
            cart_ids.append(cart['id'])

        # pay transaction if cart items are valid
        items = Item.objects.filter(id__in = cart_item_ids)
        items.update(on_sale = False, buyer = user)

        # empty the cart
        Cart.objects.filter(id__in = cart_ids).delete()

        # send email
        # to sellers (there can be multiple items in the cart belonging to different sellers so we need to send email one by one in each iteration)
        order_details = ''
        order_total = 0
        for i, item in enumerate(items):
            mail.send_mail(subject = 'New order received', message = f'Greetings {item.seller.username}, \n\nYou received a new order, {user.username} bought {item.title} for {item.price} euros. \n\nBR \nWebShop', from_email = EMAIL_HOST_USER, recipient_list = [item.seller.email])
            order_details += f'{i+1}. {item.title} = {item.price} euros\n'
            order_total += item.price

        # to buyer (there will be a single buyer, so we need to send the email once)
        mail.send_mail(subject = 'Thank you for shopping with us!', message = f'Greetings {user.username}, \n\nYour order detailes are as follows: \n{order_details}\nTotal amount = {round(order_total, 2)}\n\nBR \nWebShop', from_email = EMAIL_HOST_USER, recipient_list = [user.email])

        return Response([], status = status.HTTP_200_OK)