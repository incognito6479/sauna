# Generated by Django 3.2.5 on 2021-07-24 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_created'),
        ('paymentlog', '0002_auto_20210724_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlog',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='order.order'),
            preserve_default=False,
        ),
    ]
