# Generated by Django 4.1.4 on 2022-12-14 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_rename_user_id_item_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='added_by',
            new_name='seller',
        ),
    ]
