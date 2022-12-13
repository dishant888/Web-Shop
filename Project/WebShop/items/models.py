from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    price = models.FloatField()
    date = models.DateField(("Date"), default = datetime.date.today)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default = None, null = True)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'added_by', 'date']