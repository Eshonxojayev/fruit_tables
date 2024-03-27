from django import forms
from .models import Fruit

class AddFruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ("title", "description", "image", "count", "price")