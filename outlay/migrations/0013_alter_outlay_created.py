# Generated by Django 3.2.5 on 2021-07-25 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlay', '0012_alter_outlay_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 5, 41, 6, 263518)),
        ),
    ]