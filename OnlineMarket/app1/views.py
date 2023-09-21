from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from app1.forms import ItemClass
from app1.models import Item


# Create your views here.
class CreateItemView(CreateView):
    model = Item
    form_class = ItemClass
    template_name = 'app1/item_form.html'

    def get_success_url(self):
        return reverse('app1:list_items')

    def get_form_kwargs(self):
        data = super(CreateItemView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


class ItemView(ListView):
    model = Item
    template_name = 'app1/item_index.html'
