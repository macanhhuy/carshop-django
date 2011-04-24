# -*- coding:utf-8 -*-

import datetime
from models import *

CART_ID = 'CART-ID'

class ItemDoesNotExist(Exception):
	pass

class CartManager:
	def __init__(self, request):
		cart_id = request.session.get(CART_ID)
		if cart_id:
			try:
				cart = Cart.objects.get(id=cart_id, checked_out=False)
			except Cart.DoesNotExist:
				cart = self.new(request)
		else:
			cart = self.new(request)
		self.cart = cart

	def __iter__(self):
		for item in self.cart.item_set.all():
			yield item

	def new(self, request):
		cart = Cart(creation_date=datetime.datetime.now())
		cart.save()
		request.session[CART_ID] = cart.id
		return cart

	def add(self, product, unit_price, quantity=1):
		item = CartItem()
		item.cart = self.cart
		item.product = product
		item.unit_price = unit_price
		item.quantity = quantity
		item.save()

	def remove(self, product):
		try:
			item = CartItem.objects.get(
				cart=self.cart,
				product=product,
			)
		except CartItem.DoesNotExist:
			raise ItemDoesNotExist
		else:
			item.delete()

	def update(self, product, quantity, unit_price=None):
		try:
			item = CartItem.objects.get(
				cart=self.cart,
				product=product,
			)
		except CartItem.DoesNotExist:
			raise ItemDoesNotExist

	def clear(self):
		for item in self.cart.item_set:
			item.delete()

