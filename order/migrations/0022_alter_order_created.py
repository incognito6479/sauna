# Generated by Django 3.2.5 on 2021-07-25 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20210725_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 5, 30, 45, 760398)),
        ),
    ]