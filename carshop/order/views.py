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
from ..customer.models import CustomerAddressHistory


@login_required(redirect_field_name='/order/checkout', login_url='/login')
def checkout(request, orderId):
    #print(Order.objects.select_related().get(pk=orderId).as_sql())
    #print(Order.objects.get(pk=orderId).as_sql())

    order = Order.objects.select_related().get(pk=orderId)

    if request.user.pk != order.customer_id:
        return render_to_response('error.html', {}, RequestContext(request))

    addresses = CustomerAddressHistory.objects.select_related().filter(customer=request.user)
    if 'POST' == request.method:
        orderForm = OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()

            try:
                customerAddressHistory = CustomerAddressHistory.objects.get(customer=request.user,
                                                                            first_name=orderForm.cleaned_data[
                                                                                       'billing_first_name'],
                                                                            last_name=orderForm.cleaned_data[
                                                                                      'billing_last_name'],
                                                                            zip=orderForm.cleaned_data[
                                                                                'billing_postcode'],
                                                                            country=orderForm.cleaned_data[
                                                                                    'billing_country'],
                                                                            state=orderForm.cleaned_data[
                                                                                  'billing_state'],
                                                                            city=orderForm.cleaned_data['billing_city'],
                                                                            street_address=orderForm.cleaned_data[
                                                                                           'billing_street_address'], )
            except CustomerAddressHistory.DoesNotExist:
                CustomerAddressHistory.objects.create(customer=request.user.get_profile(),
                                                      first_name=orderForm.cleaned_data['billing_first_name'],
                                                      last_name=orderForm.cleaned_data['billing_last_name'],
                                                      zip=orderForm.cleaned_data['billing_postcode'],
                                                      country=orderForm.cleaned_data['billing_country'],
                                                      state=orderForm.cleaned_data['billing_state'],
                                                      city=orderForm.cleaned_data['billing_city'],
                                                      street_address=orderForm.cleaned_data['billing_street_address'], )

        else:
            return render_to_response('order.html', {'orderForm': orderForm, 'orderId': order.pk, 'addresses': addresses}, RequestContext(request))
    elif 'GET' == request.method:
        orderForm = OrderForm(instance=order)
        return render_to_response('order.html', {'orderForm': orderForm, 'orderId': order.pk, 'addresses': addresses}, RequestContext(request))

    paypal_dict = {
        'business': 'xtwxfx_1303744118_biz@gmail.com',
        'amount': order.order_total_price,
        'item_name': orderId,
        'invoice': orderId,
        'notify_url': 'http://localhost:8000/paypal_ipn',
        'return_url': 'http://localhost:8000/order/paypalReturn',
        'cancel_return': 'http://localhost:8000/order/paypalCancel',
        }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = RequestContext(request, {'form': form})

    return render_to_response('checkout.html', context)


@login_required(redirect_field_name='/order/checkout', login_url='/login')
def generate_order(request):
    return render_to_response('order.html', {}, RequestContext(request))


@never_cache
@anti_resubmit('save_order')
@login_required(redirect_field_name='/order/checkout', login_url='/login')
def save_order(request):
    cart = Cart.objects.get_or_create_from_request(request)
    addresses = CustomerAddressHistory.objects.select_related().filter(customer=request.user)
    try:
        order = Order.objects.create_from_cart(request, cart,
                                               customer=request.user.get_profile(),
                                               billing_first_name=request.user.first_name,
                                               billing_last_name=request.user.last_name,
                                               order_total_price=cart.total_price,
                                               ip_address=request.META['REMOTE_ADDR'],
                                               order_status=1)
    except Customer.DoesNotExist:
        return render_to_response('error.html', {}, RequestContext(request))

    if order is None:
        return render_to_response('prompt.html', {'prompt': 'you cart is empty'}, RequestContext(request))

    orderForm = OrderForm(instance=order)
    return render_to_response('order.html', {'orderForm': orderForm, 'orderId': order.pk, 'addresses': addresses}, RequestContext(request))


@login_required(redirect_field_name='/order/orderStatus', login_url='/login')
def order_status(request, pageIndex=1):
    try:
        orders = Order.objects.get_order_and_order_products(customer=request.user.get_profile(), order_status=1, page_index=pageIndex)
    except Customer.DoesNotExist:
        return render_to_response('error.html', {}, RequestContext(request))

    return render_to_response('order_status.html', {'orders': orders}, RequestContext(request))


def change_qty(request, orderId, orderProductId, count):
    try:
        order = Order.objects.get(pk=orderId)
        orderProduct = OrderProduct.objects.get(pk=orderProductId, order=orderId)
    except Order.DoesNotExist:
        return render_to_response('error')
    except OrderProduct.DoesNotExist:
        return render_to_response('error')
    else:
        orderProduct.product_quantity = orderProduct.product_quantity + int(count)

        if orderProduct.product_quantity < 0:
            orderProduct.product_quantity = 0
            return HttpResponse(simplejson.dumps({'total': str(order.order_total_price), 'qty': 0}))
        else:
            order.order_total_price = order.order_total_price + orderProduct.product_unit_price * int(count)
            order.save()
            orderProduct.save()
            return HttpResponse(
                simplejson.dumps({'total': str(order.order_total_price), 'qty': str(orderProduct.product_quantity)}))


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
    try:
        if 'POST' == request.method:
            paypalIpnForm = PayPalIPNForm(request.POST)
            paypalIpnForm.save()

            if 'Pending' == paypalIpnForm.instance.payment_status:
                order = Order.objects.get(pk=paypalIpnForm.instance.invoice)
                order.order_status = 2
                order.save()

            return render_to_response('success.html', {}, RequestContext(request))
        else:
            return render_to_response('error.html', {}, RequestContext(request))
    except Exception, e:
        print e
        return render_to_response('error.html', {'e': 'exception'}, RequestContext(request))

def paypal_cancel(request):
    try:
        if 'POST' == request.method:
            print(request.POST)
            paypalIpnForm = PayPalIPNForm(request.POST)
            paypalIpnForm.save()
            return HttpResponse('return cancel')
        else:
            return render_to_response('error.html', {}, RequestContext(request))
    except Exception, e:
        return HttpResponse('exception')
