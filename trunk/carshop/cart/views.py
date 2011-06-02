# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from paypal.pro.views import PayPalPro
from paypal.standard.forms import PayPalPaymentsForm
from carshop.product.models import Product

from .models import *

#@login_required(login_url='/login/')
def add_cart(request, productId, quantity):
    #if not request.user.is_authenticated():
    #	redirect = {'login' : '/login/'}
    #	return HttpResponse(simplejson.dumps(redirect))

    product = Product.objects.get(id=productId)

    #CartManager.cart.add(product, product.product_price, quantity)
    try:
        cart = Cart.objects.get_or_create_from_request(request)
        cart.put_into_cart(product, quantity)
    except Exception, e:
        print e

    return HttpResponse('add success')


def del_cart(request, itemId):
    cart = Cart.objects.get_or_create_from_request(request)
    cart.put_out_cart(itemId)

    return HttpResponseRedirect('/cart/cart.html')
    #items = cart.show_cart_items()
    #return render_to_response('cart.html', {'items': items}, RequestContext(request))


def cart_view(request):
    cart = Cart.objects.get_or_create_from_request(request)
    items = cart.show_cart_items()

    #print request.META
    return render_to_response('cart.html', {'items': items}, RequestContext(request))


    
    
def checkout(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/order/generateOrder'#request.path
        return HttpResponseRedirect('/login.html')

    cart = Cart.objects.get_or_create_from_request(request)
    items = cart.show_cart_items()
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
		
