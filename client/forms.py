from django import forms
from .models import Client


class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
