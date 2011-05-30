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
    
    orderForm = OrderForm(request)
    
    
    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))

def generate_order(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/cart/cart.html'
        return HttpResponseRedirect('/login.html')
    
    return render_to_response('order.html', {}, RequestContext(request))