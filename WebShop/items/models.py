from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.FloatField()
    date = models.DateField(("Date"), default = datetime.date.today)
    on_sale = models.BooleanField(default = True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True, related_name = 'seller')
    buyer = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True, blank = True, related_name = 'buyer')

    def __str__(self):
        return self.title

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'seller', 'buyer', 'on_sale','date']