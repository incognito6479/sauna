# Generated by Django 3.2.5 on 2021-07-25 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlay', '0006_alter_outlay_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 5, 29, 11, 104852)),
        ),
    ]
