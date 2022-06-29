from django.db import models
from datetime import datetime


class OutlayCategory(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Outlay(models.Model):
    category = models.ForeignKey(OutlayCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=500, verbose_name='Причина')
    summa = models.IntegerField(verbose_name='Сумма')
    created = models.DateTimeField(default=datetime.today().strftime('%Y-%m-%d'))

    def __str__(self):
        return self.name
