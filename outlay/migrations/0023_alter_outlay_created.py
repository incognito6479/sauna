# Generated by Django 3.2.5 on 2021-07-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlay', '0022_auto_20210728_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='created',
            field=models.DateTimeField(default='2021-07-29'),
        ),
    ]
