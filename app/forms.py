from django import forms
from app.models import Station, Product


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        exclude=[""]
        skip_unchanged = True 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [""]
        skip_unchanged = True