# Generated by Django 4.2.5 on 2023-09-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
