# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_value'),
        ('orders', '0004_orderitemproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItemProxy',
        ),
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Report Order Item',
                'proxy': True,
                'verbose_name_plural': 'Report Order Items',
            },
            bases=('products.product',),
        ),
        migrations.AlterModelOptions(
            name='orderproxy',
            options={'verbose_name': 'Report Order', 'verbose_name_plural': 'Report Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
