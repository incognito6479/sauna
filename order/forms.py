from django import forms
from .models import OrderItem


class OrderItemAddForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'count', 'price')
