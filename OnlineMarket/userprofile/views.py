from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from userprofile.forms import CreateNewAccountForm


# Create your views here.
class CreateNewAccountView(CreateView):
    model = User
    template_name = 'app1/item_form.html'
    form_class = CreateNewAccountForm

    def form_valid(self, form):
        print(form)
        return super(CreateNewAccountView, self).form_valid(form)

    def get_success_url(self):
        if (user_instance := User.objects.filter(id=self.object.id)) and user_instance.exists():
            user_object = user_instance.first()
            user_object.set_password(user_object.password)
            user_object.save()

        return reverse('login')


class AccountView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/userprofile_index.html'


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'app1/item_form.html'
    form_class = CreateNewAccountForm

    # def get_form_kwargs(self, **kwargs):
    #     data = super(UpdateUserView, self).get_form_kwargs()
    #     data.update({'pk': self.kwargs['pk']})
    #     return data
    def form_valid(self, form):
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.set_password(form.cleaned_data['password'])
            user_instance.save()
        return super(UpdateUserView, self).form_valid(form)

    def get_success_url(self):
        # return reverse('app1:user_account')
        return reverse_lazy('userprofile:edit_account', kwargs={'pk': self.object.pk})

@login_required
def delete_user(request, pk):
    User.objects.filter(id=pk).delete()
    return redirect('login')
