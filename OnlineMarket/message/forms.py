from django import forms
from django.forms import TextInput

from message.models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content',]

        widgets = {
            'content': TextInput(attrs={'placeholder': 'Item name', 'class': 'form-control text-white bg-dark'}),
        }
