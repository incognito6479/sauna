# Generated by Django 3.2.5 on 2021-07-28 22:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20210717_1808'),
        ('sauna', '0005_alter_saunapricetypes_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0035_auto_20210726_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 22, 32, 12, 425966)),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.CharField(max_length=500, verbose_name='Конец бронирования'),
        ),
        migrations.AlterField(
            model_name='order',
            name='hours',
            field=models.IntegerField(verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sauna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauna.sauna', verbose_name='Сауна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.CharField(max_length=500, verbose_name='Начало бронирования'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
