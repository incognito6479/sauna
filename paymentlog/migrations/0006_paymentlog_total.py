# Generated by Django 3.2.5 on 2021-07-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentlog', '0005_alter_paymentlog_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlog',
            name='total',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
