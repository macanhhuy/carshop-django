# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from paypal.pro.views import PayPalPro
from paypal.standard.forms import PayPalPaymentsForm
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

def del_cart(request, itemId):
	cartManager = CartManager(request)
	
	cartManager.remove(Product.objects.get(pk=itemId))

	items = cartManager.getItems(request)
	return render_to_response('cart.html', {'items': items}, RequestContext(request))

def cart_view(request):
	cartManager = CartManager(request)

	items = cartManager.getItems(request)

	return render_to_response('cart.html', {'items': items}, RequestContext(request))

def checkout(request):
	if not request.user.is_authenticated():
		request.session['redirect_url'] = request.path
		return HttpResponseRedirect('/login.html')

	cartManager = CartManager(request)
	items = cartManager.getItems(request)
	amount = 0.0
	for item in items:
		amount + amount + float(item.quantity * item.unit_price)

	item = {"amt": amount,
		"inv": "inventory",
		"custom": "tracking",
		"cancelurl": "http://localhost:8000/paypal_cancel",
		"returnurl": "http://localhost:8000/paypal_return"}

	kw = {"item": item,
		"payment_template": "checkout.html",
		"confirm_template": "confirmation.html",
		"success_url": "/paypal_success"
	}
	ppp = PayPalPro(**kw)
	return ppp(request)
		
