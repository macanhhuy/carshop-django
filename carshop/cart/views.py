# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from carshop.product.models import Product
from cart import CartManager

#@login_required(login_url='/login/')
def add_cart(request, productId, quantity):

	if not request.user.is_authenticated():
		redirect = {'login' : '/login/'}
		return HttpResponse(redirect)

	product = Product.objects.get(id=productId)
	
	#CartManager.cart.add(product, product.product_price, quantity)
	cartManager = CartManager(request)
	cartManager.add(product, product.product_price, quantity)
	
	return HttpResponse('success')
	
	
def cart_view(request):
	pass
	