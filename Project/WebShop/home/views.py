from django.shortcuts import render
from django.contrib.auth. models import User
from items.models import Item

# Create your views here.
def index(req):
    context = {
        'users': User.objects.filter(is_superuser = False).count(),
        'items': Item.objects.filter(on_sale = True).count()
    }
    return render(request = req, template_name = 'home/index.html', context = context)