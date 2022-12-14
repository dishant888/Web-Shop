# Generated by Django 4.1.4 on 2022-12-14 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0010_item_buyer_item_on_sale_alter_item_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='buyer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
