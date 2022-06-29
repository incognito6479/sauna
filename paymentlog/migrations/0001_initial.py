# Generated by Django 3.2.5 on 2021-07-10 21:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_log_type', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=500)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('outcat', models.IntegerField()),
                ('outlay', models.IntegerField()),
                ('outlay_child', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]