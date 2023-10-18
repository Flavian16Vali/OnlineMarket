from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, Select

from OnlineMarket.utils import get_exchange_rates
from userprofile.models import CustomUser

PREFERRED_CURRENCY = [(key, key) for key in get_exchange_rates().keys()]


class CreateNewAccountForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "m-1 form-control text-white bg-dark",
    #                                                              'placeholder': "Insert the password",
    #                                                              'type': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                                                         'placeholder': "Insert the password",
                                                                         'type': 'password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'preferred_currency', 'password']

        widgets = {
            'username': TextInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                         'placeholder': "Username"}),
            'email': TextInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                      'placeholder': "Email"}),
            'preferred_currency': Select(attrs={'class': 'form-control text-white bg-dark'}),
            'password': PasswordInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                             'placeholder': "Insert the password",
                                             'type': 'password'}),
        }

    def clean(self):
        field_data = self.cleaned_data
        username_value = field_data.get('username')
        email_value = field_data.get('email')

        current_object_id = self.instance.id
        existing_usernames = User.objects.filter(username=username_value).exclude(id=current_object_id).exists()
        existing_email = User.objects.filter(username=email_value).exclude(id=current_object_id).exists()

        if existing_usernames:
            msg = 'This username is already used'
            self._errors['username'] = self.error_class([msg])
        if existing_email:
            msg = 'This email is already used'
            self._errors['username'] = self.error_class([msg])

        password_value = self.cleaned_data.get('password')
        confirm_password_value = self.cleaned_data.get('confirm_password')
        if password_value != confirm_password_value:
            msg = 'The passwords are not the same!'
            self._errors['password'] = self.error_class([msg])

        return field_data
