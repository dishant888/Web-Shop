from django.contrib import admin
from cart.models import Cart, CartAdmin

# Register your models here.
admin.site.register(Cart, CartAdmin)