# Generated by Django 3.2.5 on 2021-07-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlay', '0020_alter_outlay_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlay',
            name='created',
            field=models.DateTimeField(default='2021-07-26'),
        ),
    ]