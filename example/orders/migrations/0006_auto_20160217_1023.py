# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20160120_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item', 'verbose_name_plural': 'Order Items'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='data',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=None, verbose_name='Date added', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False, verbose_name='Delivered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.NullBooleanField(default=None, verbose_name='Gender', choices=[(0, 'Male'), (1, 'Female')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Payment Type', blank=True, choices=[(1, 'Bankslip'), (2, 'Credit Card'), (3, 'Debit')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_value',
            field=models.DecimalField(verbose_name='Total Value', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(verbose_name='Quantity sold'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total',
            field=models.DecimalField(default=0, verbose_name='Total', max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='value',
            field=models.DecimalField(verbose_name='Value', max_digits=11, decimal_places=2),
        ),
    ]
