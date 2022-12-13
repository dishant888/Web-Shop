from django.contrib import admin
from items.models import Item, ItemAdmin

# Register your models here.
admin.site.register(Item, ItemAdmin)