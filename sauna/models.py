from django.db import models
from .choices import SAUNA_STATUS, COLOR


class Sauna(models.Model):
    name = models.CharField(max_length=500, verbose_name='Сауна')
    status = models.CharField(max_length=500, choices=SAUNA_STATUS, default='active', verbose_name='Сауна статус')
    color = models.CharField(max_length=200, choices=COLOR, default='yellow', verbose_name='Цвет')

    class Meta:
        verbose_name = 'Сауна'
        verbose_name_plural = 'Сауна'

    def __str__(self):
        return self.name


class SaunaPriceTypes(models.Model):
    sauna = models.ForeignKey(Sauna, on_delete=models.CASCADE, verbose_name='Сауна')
    min_people = models.IntegerField(verbose_name='Мин. человек')
    max_people = models.IntegerField(verbose_name='Макс. человек')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Сауна цена'
        verbose_name_plural = 'Сауна цена'

    def __str__(self):
        return self.sauna.name
