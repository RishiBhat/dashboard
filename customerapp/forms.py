from django.utils.translation import TranslatorCommentWarning
from .models import Contact, Orders, OrderUpdate

from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = [""]
        skip_unchanged = True


class OrdersForm(forms.ModelForm):
    class Meta:
        model=Orders
        exclude=[""]
        skip_unchanged= True

class OrderUpdareForm(forms.Form):
    class Meta:
        model= OrderUpdate
        exclude=['']
        skip_unchanged= True