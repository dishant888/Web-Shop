from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from django.contrib import admin

# Create your models here.
class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    price = models.FloatField()

class CartAdmin(admin.ModelAdmin):
    list_display = ['item', 'user', 'price']