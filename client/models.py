from django.db import models
from .choices import CLIENT_STATUS, CLIENT_TYPE


class Client(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя')
    phone = models.CharField(max_length=500, unique=True, verbose_name='Телефон')
    client_type = models.CharField(max_length=500, choices=CLIENT_TYPE, default='normal', verbose_name='Тип клиента')
    status = models.CharField(max_length=500, choices=CLIENT_STATUS, default='active', verbose_name='Статус')
    content = models.CharField(max_length=700, blank=True, null=True, verbose_name='Содержание')

    def __str__(self):
        return f"{self.name} / {self.get_client_type_display()}"


