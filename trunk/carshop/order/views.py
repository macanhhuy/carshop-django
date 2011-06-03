# -*- coding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *
from .forms import *
from ..cart.models import Cart

def checkout(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/order/checkout'
        return HttpResponseRedirect('/login.html')

    cart = Cart.objects.get_or_create_from_request(request)

    order = Order.objects.create(customer=request.user.get_profile(), billing_first_name=request.user.first_name, billing_last_name=request.user.last_name, order_total_price=cart.total_price, ip_address=request.META['REMOTE_ADDR'])
#    order.customer = request.user.get_profile()
#    order.billing_first_name = request.user.first_name
#    order.billing_last_name = request.user.last_name
#    order.order_total_price = cart.total_price
#    order.ip_address = request.META['REMOTE_ADDR']
#    order.save()
    orderForm = OrderForm(instance=order)
    
    
    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))

def generate_order(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/cart/cart.html'
        return HttpResponseRedirect('/login.html')
    
    return render_to_response('order.html', {}, RequestContext(request))