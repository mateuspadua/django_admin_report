.. _tutorial:

Tutorial
===============================================

Installation
------------

#. Install ``django_admin_report``: ::

	$ pip install django_admin_report

#. Add ``admin_report`` to your ``INSTALLED_APPS``:

.. code-block:: python

	INSTALLED_APPS = (
	    'admin_report',  # first
	    'import_export',
	    'django.contrib.admin',
	    ...
	)

How to use
----------

In the ``example`` folder have a code example that will help you to make reports.


.. code-block:: python

	# products/models.py
	class Product(models.Model):
	    name = models.CharField(verbose_name=u'Name', max_length=255)
	    value = models.DecimalField(
	        verbose_name=u'Value', max_digits=11, decimal_places=2)

	    def __unicode__(self):
	        return self.name


	# orders/models.py
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


#. In your app, add in ``model.py`` one proxy to model that you desire create report

.. code-block:: python

	class ProductProxy(Product):
		class Meta:
			verbose_name, verbose_name_plural = u"Report Order Item", u"Report Order Items"
			proxy = True 	

#. In ``admin.py``, create one using ``ChartReportAdmin``

.. code-block:: python

	from django.db.models import Sum, Avg, Count, Min, Max
	from admin_report.mixins import ChartReportAdmin


	class ReportOrderItemsAdmin(ChartReportAdmin):
		list_display = ('name', 'orderitem__value__avg', 'orderitem__value__max', 'orderitem__value__min', 'orderitem__quantity__sum', 'orderitem__total__sum',)

		report_annotates = (
			("orderitem__quantity", Sum, "subtotal total items sold"),
			("orderitem__total", Sum, "subtotal total value sold"),
			("orderitem__value", Avg, "product sold average"),
			("orderitem__value", Max, "higher sold value"),
			("orderitem__value", Min, "lower sold value"),
		)

		report_aggregates = (
			('orderitem__total__sum', Sum, "<b>Total: R$ %value</b>"),
			('orderitem__quantity', Sum, "total items sold"),
		)

	admin.site.register( ProductProxy, ReportOrderItemsAdmin )



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

