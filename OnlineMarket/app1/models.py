from django.db import models


ITEM_CHOICES = (('Toys', 'Toys'), ('Sport', 'Sport'), ('Animals', 'Animals'))


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=20, choices=ITEM_CHOICES)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    active = models.BooleanField(default=True)
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}'
