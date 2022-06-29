# Generated by Django 3.2.5 on 2021-07-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlog',
            name='outcat',
        ),
        migrations.RemoveField(
            model_name='paymentlog',
            name='outlay',
        ),
        migrations.RemoveField(
            model_name='paymentlog',
            name='outlay_child',
        ),
        migrations.RemoveField(
            model_name='paymentlog',
            name='payment_log_type',
        ),
        migrations.AddField(
            model_name='paymentlog',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличный расчет'), ('cashless', 'Безналичный расчет')], default='cash', max_length=500),
        ),
        migrations.AddField(
            model_name='paymentlog',
            name='payment_type',
            field=models.CharField(choices=[('payment', 'Оплата'), ('advance', 'Аванс')], default='advance', max_length=500),
        ),
    ]
