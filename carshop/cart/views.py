# -*- coding:utf-8 -*-

import simplejson

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from ..paypal.pro.views import PayPalPro
from ..paypal.standard.forms import PayPalPaymentsForm
from carshop.product.models import Product

from .models import *

#@login_required(login_url='/login/')
def add_item(request, productId, quantity):
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
        return HttpResponse(simplejson.dumps({'result': 'false', 'cartCount': cart.cart_count}))

    return HttpResponse(simplejson.dumps({'result': 'true', 'cartCount': cart.cart_count}))

def change_item_qty(request, productId, quantity):
    product = Product.objects.get(id=productId)

    try:
        cart = Cart.objects.get_or_create_from_request(request)
        item_qty = cart.put_into_cart(product, quantity)
    except Exception, e:
        print e
        return HttpResponse(simplejson.dumps({'totalPrice': str(cart.total_price), 'itemQty': str(item_qty), 'cartCount': str(cart.cart_count)}))
    else:
        return HttpResponse(simplejson.dumps({'totalPrice': str(cart.total_price), 'itemQty': str(item_qty), 'cartCount': str(cart.cart_count)}))


def remove_item(request, itemId):
    try:
        cart = Cart.objects.get_or_create_from_request(request)
        cart.put_out_cart(itemId)
        if cart.cart_count is None:
            cart.clean_cart(request)
            return HttpResponse(simplejson.dumps({'totalPrice': '', 'cartCount': ''}))

    except Exception, e:
        print e
        return render_to_response('error')
    else:
        return HttpResponse(simplejson.dumps({'totalPrice': str(cart.total_price), 'cartCount': str(cart.cart_count)}))

    #return HttpResponseRedirect('/cart/cart.html')
    #items = cart.cart_items
    #return render_to_response('cart.html', {'items': items}, RequestContext(request))


def cart_view(request):
    cart = Cart.objects.get_or_create_from_request(request)

    #print request.META
    return render_to_response('cart.html', {'items': cart.cart_items, 'cart': cart}, RequestContext(request))

def clean_cart(request):
    cart = Cart.objects.get_or_create_from_request(request)
    cart.clean_cart(request)
    
    return HttpResponseRedirect('/cart/cart.html')
    
#def checkout(request):
#    if not request.user.is_authenticated():
#        request.session['redirect_url'] = '/order/generateOrder'#request.path
#        return HttpResponseRedirect('/login.html')

#    cart = Cart.objects.get_or_create_from_request(request)
#    items = cart.cart_items
#    amount = 0.0
#    for item in items:
#        amount + amount + float(item.quantity * item.unit_price)

#    item = {"amt": amount,
#            "inv": "inventory",
#            "custom": "tracking",
#            "cancelurl": "http://localhost:8000/paypal_cancel",
#            "returnurl": "http://localhost:8000/paypal_return"}

#    kw = {"item": item,
#          "payment_template": "checkout.html",
#          "confirm_template": "confirmation.html",
#          "success_url": "/paypal_success"
#    }
#    ppp = PayPalPro(**kw)
#    return ppp(request)
		
