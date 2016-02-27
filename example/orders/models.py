# coding: utf-8
from django.db import models
from products.models import Product


PAYMENT_TYPE = (
        (1, u"Bankslip"),
        (2, u"Credit Card"),
        (3, u"Debit"),
    )

GENDER = (
    (0, u"Male"),
    (1, u"Female")
)


class Order(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name=u'Date added')
    payment_type = models.PositiveSmallIntegerField(
        verbose_name=u'Payment Type', default=None,
        choices=PAYMENT_TYPE, blank=True, null=True)
    email = models.EmailField(verbose_name=u'Email', null=True)
    delivered = models.BooleanField(verbose_name=u'Delivered', default=False)
    total_value = models.DecimalField(
        verbose_name=u'Total Value', max_digits=11, decimal_places=2)
    gender = models.NullBooleanField(
        verbose_name=u'Gender', choices=GENDER,
        null=True, blank=True, default=None)

    def __unicode__(self):
        return str(self.id)


class OrderItem(models.Model):
    class Meta:
        verbose_name, verbose_name_plural = u"Order Item", u"Order Items"

    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(verbose_name=u'Quantity sold')
    value = models.DecimalField(
        verbose_name=u'Value', max_digits=11, decimal_places=2)
    total = models.DecimalField(
        verbose_name=u'Total', max_digits=11,
        decimal_places=2, blank=True, default=0)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.value
        super(OrderItem, self).save(*args, **kwargs)


class OrderProxy(Order):
    class Meta:
        verbose_name, verbose_name_plural = u"Report Order", u"Report Orders"
        proxy = True


class ProductProxy(Product):
    class Meta:
        verbose_name, verbose_name_plural = (u"Report Order Item",
                                             u"Report Order Items")
        proxy = True
