# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from ..decorators import login_required
from .models import *
from .forms import *
from ..cart.models import Cart

@login_required(redirect_field_name='/order/checkout', login_url='/login')
def checkout(request):
    #if not request.user.is_authenticated():
    #    return redirect('/login/order/checkout')

    cart = Cart.objects.get_or_create_from_request(request)

    order = Order.objects.create(cart=cart,
                                 customer=request.user.get_profile(),
                                 billing_first_name=request.user.first_name,
                                 billing_last_name=request.user.last_name,
                                 order_total_price=cart.total_price,
                                 ip_address=request.META['REMOTE_ADDR'])

    orderForm = OrderForm(instance=order)

    return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))


@login_required(redirect_field_name='/order/checkout', login_url='/login')
def generate_order(request):
#    if not request.user.is_authenticated():
#        request.session['redirect_url'] = '/cart/cart.html'
#        return HttpResponseRedirect('/login.html')

    return render_to_response('order.html', {}, RequestContext(request))


@login_required((redirect_field_name='/order/checkout', login_url='/login')
def save_order(request):
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)

        print 'sdfsdf'
    else:
        return redirect('/index.html')