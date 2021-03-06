# Generated by Django 3.2.5 on 2021-07-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=500, null=True)),
                ('client_type', models.CharField(choices=[('regular', 'Постоянный'), ('normal', 'Обычный'), ('vip', 'VIP')], default='normal', max_length=500)),
                ('status', models.CharField(choices=[('active', 'Активный'), ('inactive', 'Неактивный')], default='active', max_length=500)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
