from datetime import datetime

from django.db import models

from OnlineMarket.utils import get_exchange_rates
# from message.models import Message

ITEM_CHOICES = (('Toys', 'Toys'), ('Sport', 'Sport'), ('Animals', 'Animals'), ('Auto', 'Auto'), ('Clothes', 'Clothes'),)
CURRENCY_CHOICES = [(key, key) for key in get_exchange_rates().keys()]


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=20, choices=ITEM_CHOICES)
    image = models.ImageField(upload_to='media/', null=False, blank=False)
    active = models.BooleanField(default=True)
    id_user = models.ForeignKey('userprofile.CustomUser', on_delete=models.CASCADE)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    posted_date = models.DateTimeField(default=datetime.now)
    edited_date = models.DateTimeField(auto_now=True, blank=True)

    # from message.models import Message
    # messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}'
