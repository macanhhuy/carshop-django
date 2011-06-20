# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from ..decorators import login_required, anti_resubmit
from .models import *
from .forms import *
from ..cart.models import Cart

@login_required(redirect_field_name='/order/checkout', login_url='/login')
def checkout(request):
    cart = Cart.objects.get_or_create_from_request(request)

    order = Order.objects.create_or_get(cart=cart,
                                 customer=request.user.get_profile(),
                                 billing_first_name=request.user.first_name,
                                 billing_last_name=request.user.last_name,
                                 order_total_price=cart.total_price,
                                 ip_address=request.META['REMOTE_ADDR'])

    orderForm = OrderForm(instance=order)

    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))


@login_required(redirect_field_name='/order/checkout', login_url='/login')
def generate_order(request):
    return render_to_response('order.html', {}, RequestContext(request))


@never_cache
@anti_resubmit('save_order')
@login_required(redirect_field_name='/order/checkout', login_url='/login')
def save_order(request):

    cart = Cart.objects.get_or_create_from_request(request)

    
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid()
            
        else:
            return render_to_response('order.html', {'orderForm', orderForm}, RequestContext(request))


    order = Order.objects.create_or_get(cart=cart,
                                 customer=request.user.get_profile(),
                                 billing_first_name=request.user.first_name,
                                 billing_last_name=request.user.last_name,
                                 order_total_price=cart.total_price,
                                 ip_address=request.META['REMOTE_ADDR'])

    orderForm = OrderForm(instance=order)
    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))

