from django import forms
from django.forms import TextInput, NumberInput, Select

from app1.models import Item, ITEM_CHOICES


class ItemClass(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'type']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Item name', 'class': 'form-control text-white bg-dark'}),
            'price': NumberInput(attrs={'placeholder': 'Item price', 'class': 'form-control text-white bg-dark'}),
            'type': Select(attrs={'class': 'form-control text-white bg-dark'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(ItemClass, self).__init__(*args, **kwargs)
        self.pk = pk
