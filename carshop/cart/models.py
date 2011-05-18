# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class Cart(models.Model):
	session = models.CharField(max_length=40, blank=True, null=True)
	user = models.ForeignKey(User, blank=True, null=True)
	creation_date = models.DateTimeField(verbose_name=_('creation date'))
	checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))
	
	class Meta:
		db_table = 'cart'
		ordering = ('-creation_date',)

	def __unicode__(self):
		return unicode(self.creation_date)

class ItemManager(models.Manager):
	def get(self, *args, **kwargs):
		if 'product' in kwargs:
			kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
			kwargs['object_id'] = kwargs['product'].pk
			del(kwargs['product'])
		return super(ItemManager, self).get(*args, **kwargs)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, verbose_name=_('cart'))
	quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
	unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
	# product as generic relation
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	object_name = models.CharField(max_length=100)

	objects = ItemManager()

	class Meta:
		db_table = 'cart_item'
		ordering = ('cart',)

	def __unicode__(self):
		return u''

	def total_price(self):
		return self.quantity * self.unit_price
	total_price = property(total_price)

	# product
	def get_product(self):
		return self.content_type.get_object_for_this_type(id=self.object_id)

	def set_product(self, product):
		self.content_type = ContentType.objects.get_for_model(type(product))
		self.object_id = product.pk
		self.object_name = product.product_name

	product = property(get_product, set_product)

