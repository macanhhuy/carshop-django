# -*- coding:utf-8 -*-

import simplejson

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from ..paypal.standard.forms import PayPalPaymentsForm
from ..paypal.standard.ipn.models import PayPalIPN
from ..paypal.standard.ipn.forms import PayPalIPNForm
from ..decorators import login_required, anti_resubmit
from .models import *
from .forms import *
from ..cart.models import Cart


@login_required(redirect_field_name='/order/checkout', login_url='/login')
def checkout(request, orderId):

    #print(Order.objects.select_related().get(pk=orderId).as_sql())
    #print(Order.objects.get(pk=orderId).as_sql())

    order = Order.objects.select_related().get(pk=orderId)

    if request.user.pk != order.customer_id:
        return HttpResponse('error')

    if 'POST' == request.method:
        orderForm = OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            #return redirect('/order/checkout/' + order.pk)
        else:
            return render_to_response('order.html', {'orderForm': orderForm}, RequestContext(request))
    elif 'GET' == request.method:
        orderForm = OrderForm(instance=order)
        return render_to_response('order.html', {'orderForm': orderForm, 'orderId': order.pk}, RequestContext(request))

    paypal_dict = {
        'business': 'xtwxfx_1303744118_biz@gmail.com',
        'amount': order.order_total_price,
        'item_name': 'Car Seats',
        'invoice': orderId,
        'notify_url': 'http://localhost:8000/paypal_ipn',
        'return_url': 'http://localhost:8000/order/paypalReturn',
        'cancel_return': 'http://localhost:8000/paypal_cancel',
        }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = RequestContext(request, {'form': form})

    return render_to_response('checkout.html', context)



@login_required(redirect_field_name='/order/checkout', login_url='/login')
def generate_order(request):
    return render_to_response('order.html', {}, RequestContext(request))


@never_cache
@anti_resubmit('save_order')
@login_required(redirect_field_name='/order/saveOrder', login_url='/login')
def save_order(request):
    cart = Cart.objects.get_or_create_from_request(request)

    try:
        order = Order.objects.create_from_cart(request, cart,
                                            customer=request.user.get_profile(),
                                            billing_first_name=request.user.first_name,
                                            billing_last_name=request.user.last_name,
                                            order_total_price=cart.total_price,
                                            ip_address=request.META['REMOTE_ADDR'],
                                            order_status=1)
    except Customer.DoesNotExist:
        return HttpResponse('error')

    orderForm = OrderForm(instance=order)
    return render_to_response('order.html', {'orderForm': orderForm, 'orderId': order.pk}, RequestContext(request))

@login_required(redirect_field_name='/order/orderStatus.html', login_url='/login')
def order_status(request):
    orders = Order.objects.get_order_and_order_products(customer=request.user.get_profile(), order_status=1)

    return render_to_response('order_status.html', {'orders': orders}, RequestContext(request))


def change_qty(request, orderId, orderProductId, count):
    try:
        order = Order.objects.get(pk=orderId)
        orderProduct = OrderProduct.objects.get(pk=orderProductId, order=orderId)
    except Order.DoesNotExist:
        return HttpResponse('error')
    except OrderProduct.DoesNotExist:
        return HttpResponse('error')
    else:
        orderProduct.product_quantity = orderProduct.product_quantity + int(count)

        if orderProduct.product_quantity < 0:
            orderProduct.product_quantity = 0
            return HttpResponse(simplejson.dumps({'total':str(order.order_total_price), 'qty':0}))
        else:
            order.order_total_price = order.order_total_price + orderProduct.product_unit_price * int(count)
            order.save()
            orderProduct.save()
            return HttpResponse(simplejson.dumps({'total':str(order.order_total_price), 'qty':str(orderProduct.product_quantity)}))

def remove_order(request, orderId):
    try:
        Order.objects.get(pk=orderId).delete()
        OrderProduct.objects.filter(order=orderId).delete()
    except Exception, e:
        print e
        return HttpResponse('error')
    else:
        return HttpResponse(Order.objects.calc_unpal_count(request))

def remove_order_product(request, orderId, orderProductId):
    try:
        order = Order.objects.get(pk=orderId)
        orderProduct = OrderProduct.objects.get(pk=orderProductId)

        order.order_total_price = order.order_total_price - orderProduct.product_unit_price * orderProduct.product_quantity
        if 0 == order.order_total_price:
            order.delete()
        else:
            order.save()
        orderProduct.delete()
    except Exception, e:
        print e
        return HttpResponse('error')
    else:
        return HttpResponse(order.order_total_price)


def paypal_return(request):
    print request
    try:
        if 'POST' == request.method:
            paypalIpnForm = PayPalIPNForm(request.POST)
            paypalIpnForm.save()
            return HttpResponse('return success')
        else:
            return HttpResponse('error')
    except Exception, e:
        return HttpResponse('exception')
