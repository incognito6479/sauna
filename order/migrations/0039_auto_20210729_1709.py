# Generated by Django 3.2.5 on 2021-07-29 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0038_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.date(2021, 7, 29)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(default=datetime.date(2021, 7, 29)),
        ),
    ]
