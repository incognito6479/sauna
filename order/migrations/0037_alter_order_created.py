# Generated by Django 3.2.5 on 2021-07-29 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0036_auto_20210728_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 16, 38, 27, 919608)),
        ),
    ]