# Generated by Django 4.2.5 on 2023-10-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_item_posted_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='posted_date',
        ),
    ]
