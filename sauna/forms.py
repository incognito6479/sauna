from django import forms
from order.models import Order


class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'sauna', 'people_count', 'hours', 'start_time', 'end_time')
