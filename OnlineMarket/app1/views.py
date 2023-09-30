from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def delete_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).delete()
    return redirect('app1:list_items')


@login_required
def activate_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).update(active=1)
    return redirect('app1:list_items')


@login_required
def deactivate_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).update(active=0)
    return redirect('app1:list_items')


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'app1/item_detail.html', {'item': item})
