# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from carshop.product.models import Product
from cart import CartManager

#@login_required(login_url='/login/')
def add_cart(request, productId, quantity):

	#if not request.user.is_authenticated():
	#	redirect = {'login' : '/login/'}
	#	return HttpResponse(simplejson.dumps(redirect))

	product = Product.objects.get(id=productId)
	
	#CartManager.cart.add(product, product.product_price, quantity)
	cartManager = CartManager(request)
	cartManager.add(product, product.product_price, quantity)
	
	return HttpResponse('add success')
	
	
def cart_view(request):
	
	
	
	return render_to_response('cart.html', {}, RequestContext(request))
	