# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from paypal.pro.views import PayPalPro
from paypal.standard.forms import PayPalPaymentsForm

import uuid

def view_that_asks_for_money(request):
    paypal_dict = {
        'business': 'xtwxfx_1303744118_biz@gmail.com',
        'amount': '300.00',
        'item_name': 'Car Seats',
        'invoice': uuid.uuid1(),
        'notify_url': 'http://localhost:8000/paypal_ipn',
        'return_url': 'http://localhost:8000/paypal_return',
        'cancel_return': 'http://localhost:8000/paypal_cancel',
        }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = RequestContext(request, {'form': form})

    return render_to_response('money.html', context)


def buy_my_item(request):
    item = {"amt": "10.00",
            "inv": "inventory",
            "custom": "tracking",
            "cancelurl": "http://localhost:8000/customer/some/obscure/name/",
            "returnurl": "http://localhost:8000/customer/some/obscure/name/"}

    kw = {"item": item,
          "payment_template": "buy.html",
          "confirm_template": "confirmation.html",
          "success_url": "/success/"
    }

    ppp = PayPalPro(**kw)

    return ppp(request)

