from django.shortcuts import render
from django.contrib.auth. models import User
from items.models import Item
import random
from accounts.api.serializers import UserSerializer

# Create your views here.
def index(req):
    context = {
        'users': User.objects.filter(is_superuser = False).count(),
        'items': Item.objects.filter(on_sale = True).count()
    }
    return render(request = req, template_name = 'home/index.html', context = context)

# Functional requirement 2 (Automatic DB population )
# API to pupulate data in the database
def generateDB(req):
    
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
                    price = round(random.uniform(10,100),2), 
                    seller = user_instance
                    )
                item_no += 1
    
    context = {
        'users': User.objects.filter(is_superuser = False).count(),
        'items': Item.objects.filter(on_sale = True).count(),
        'DB_generated': True
    }
    return render(request = req, template_name = 'home/index.html', context = context)