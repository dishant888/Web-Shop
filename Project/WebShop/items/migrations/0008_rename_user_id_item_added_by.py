# Generated by Django 4.1.4 on 2022-12-13 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_item_user_id_alter_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user_id',
            new_name='added_by',
        ),
    ]
