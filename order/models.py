from django.db import models
from client.models import Client
from sauna.models import Sauna
from product.models import Product
from django.contrib.auth.models import User
from .choices import ORDER_STATUS
from datetime import date


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    people_count = models.IntegerField(verbose_name='Количество человека')
    sauna_hour_price = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    sauna = models.ForeignKey(Sauna, on_delete=models.CASCADE, verbose_name='Сауна')
    start_time = models.CharField(max_length=500, verbose_name='Начало бронирования')
    end_time = models.CharField(max_length=500, verbose_name='Конец бронирования')
    hours = models.IntegerField(verbose_name='Длительность')
    discount = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=500, choices=ORDER_STATUS, default='active', verbose_name='Статус')
    created = models.DateTimeField(default=date.today().today())

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created = models.DateTimeField(default=date.today().today())
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()

    def natural_key(self):
        return self.product.category.title, self.product.title


class Penalty(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.CharField(max_length=500, verbose_name='Причина')
    sum = models.IntegerField(verbose_name='Сумма')
