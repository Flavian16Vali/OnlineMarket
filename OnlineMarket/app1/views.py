from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from app1.forms import ItemClass
from app1.models import Item


# Create your views here.
class CreateItemView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemClass
    template_name = 'app1/item_form.html'

    def form_valid(self, form):
        if form.is_valid():
            item_instance = form.save(commit=False)
            item_instance.id_user_id = self.request.user.id
            item_instance.save()
        return super(CreateItemView, self).form_valid(form)

    def get_success_url(self):
        return reverse('app1:list_items')

    def get_form_kwargs(self):
        data = super(CreateItemView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


class ItemView(ListView):
    model = Item
    template_name = 'app1/item_index.html'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')

        queryset = Item.objects.filter(name__icontains=search_query)

        return queryset

# def search_items(request):
#     query = request.GET.get('query', '')
#     items = Item.objects
#
#     if query:
#         items = items.filter(name__icontains=query)
#
#     return render(request, 'app1/item_index.html', {
#         'items': items,
#         'query': query,
#     })


class UpdateItemView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemClass
    template_name = 'app1/item_form.html'

    def test_func(self):
        if ((get_item := Item.objects.filter(id=self.kwargs['pk'])) and
                get_item.exists() and
                get_item.first().id_user_id == self.request.user.id):
            return True
        return False

    def get_success_url(self):
        # return reverse('app1:list_items')
        return reverse_lazy('app1:detail_item', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        data = super(UpdateItemView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data


@login_required
def delete_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).delete()
    return redirect('app1:list_items')


@login_required
def activate_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).update(active=1)
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'app1/item_detail.html', {'item': item})


@login_required
def deactivate_item(request, pk):
    Item.objects.filter(id=pk, id_user=request.user.id).update(active=0)
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'app1/item_detail.html', {'item': item})


class ItemDetailView(DetailView):
    template_name = 'app1/item_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Item, id=pk)
