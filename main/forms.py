from django.forms import ModelForm
from main.models import Item

from django.shortcuts import redirect
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "goals", "marketPrice"]
