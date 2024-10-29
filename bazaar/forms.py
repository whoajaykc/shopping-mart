from django import forms
from django.contrib.auth.models import User
from . import models



class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['englishname','photo','price','quantity','hindiname']

class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Order
        fields=['address','mobile','customername']
        widgets = {
        'address':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

