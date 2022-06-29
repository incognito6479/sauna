from django.db import models
from django.contrib.auth.models import User
from .choices import PAYMENT_TYPE, PAYMENT_METHOD
from order.models import Order
from datetime import datetime, date


class PaymentLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    discount = models.IntegerField(default=0, blank=True, null=True)
    total = models.IntegerField()
    payment_type = models.CharField(max_length=500, choices=PAYMENT_TYPE, default='advance', verbose_name='Тип оплаты')
    payment_method = models.CharField(max_length=500, choices=PAYMENT_METHOD, default='cash', verbose_name='Метод оплаты')
    comment = models.CharField(max_length=500)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created = models.DateTimeField(default=date.today().today(), verbose_name='Дата создания')

