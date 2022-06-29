from django import forms
from .models import PaymentLog


class PaymentLogForm(forms.ModelForm):
    class Meta:
        model = PaymentLog
        fields = ('payment_type', 'payment_method')
