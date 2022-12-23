# Generated by Django 4.1.4 on 2022-12-12 21:35

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]