# coding: utf-8
from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=255)
    value = models.DecimalField(
        verbose_name=u'Value', max_digits=11, decimal_places=2)

    def __unicode__(self):
        return self.name
