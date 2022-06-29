# Generated by Django 3.2.5 on 2021-07-16 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('sauna', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_count',
        ),
        migrations.AddField(
            model_name='order',
            name='color',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='order',
            name='people_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество человека'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='client.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.CharField(max_length=500, verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='order',
            name='hours',
            field=models.IntegerField(verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sauna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sauna.sauna', verbose_name='Сауна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sauna_hour_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.CharField(max_length=500, verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('active', 'Активный'), ('inactive', 'Неактивный')], default='active', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]