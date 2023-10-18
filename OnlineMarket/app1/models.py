from datetime import datetime

from django.db import models

from OnlineMarket.utils import get_exchange_rates
from userprofile.models import CustomUser

# from userprofile.models import CustomUser

ITEM_CHOICES = (('Toys', 'Toys'), ('Sport', 'Sport'), ('Animals', 'Animals'))
CURRENCY_CHOICES = [(key, key) for key in get_exchange_rates().keys()]


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=20, choices=ITEM_CHOICES)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    active = models.BooleanField(default=True)
    id_user = models.ForeignKey('userprofile.CustomUser', on_delete=models.CASCADE)
    # id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    posted_date = models.DateTimeField(default=datetime.now)
    edited_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}'
