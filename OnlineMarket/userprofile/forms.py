from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class CreateNewAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': TextInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                         'placeholder': "Username"}),
            'email': TextInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                      'placeholder': "Email"}),
            'password': PasswordInput(attrs={'class': "m-1 form-control text-white bg-dark",
                                             'placeholder': "Insert the password",
                                             'type': 'password'}),
        }

    # def __init__(self, pk, *args, **kwargs):
    #     super(CreateNewAccountForm, self).__init__(*args, **kwargs)
    #     self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        username_value = field_data.get('username')
        email_value = field_data.get('email')
        if User.objects.filter(username=username_value).exists():
            msg = 'This username is already used'
            self._errors['username'] = self.error_class([msg])
        if User.objects.filter(email=email_value).exists():
            msg = 'This email is already used'
            self._errors['email'] = self.error_class([msg])

        return field_data