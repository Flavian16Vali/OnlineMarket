from django.contrib.auth.models import AbstractUser
from django.db import models

from OnlineMarket.utils import get_exchange_rates

CURRENCY_CHOICES = [(key, key) for key in get_exchange_rates().keys()]


class CustomUser(AbstractUser):
    preferred_currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
