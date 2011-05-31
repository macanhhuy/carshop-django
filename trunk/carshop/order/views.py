# -*- coding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from forms import *

def checkout(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/order/checkout'
        return HttpResponseRedirect('/login.html')
    
    order = Order()
    order.customer = request.user.get_profile()
    order.customer_name = request.user.get_full_name()
    order.order_total_price = 111
    order.ip_address = request.META['REMOTE_ADDR']
    order.save()
    orderForm = OrderForm(instance=order)
    
    
    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))

def generate_order(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/cart/cart.html'
        return HttpResponseRedirect('/login.html')
    
    return render_to_response('order.html', {}, RequestContext(request))