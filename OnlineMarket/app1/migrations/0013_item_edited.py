# Generated by Django 4.2.5 on 2023-10-16 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_item_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
