# Generated by Django 3.2.5 on 2021-07-22 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 17, 14, 21, 216062)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='count',
            field=models.IntegerField(),
        ),
    ]
