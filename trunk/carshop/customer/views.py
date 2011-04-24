# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from paypal.pro.views import PayPalPro
from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request):
	
	paypal_dict = {
		'business': 'xtwxfxk@gmail.com',
		'amount': '10000000.00',
		'item_name': 'Car Seat',
		'invoice': 'unique-invoice-id',
		'notify_url': 'http://localhost:8000/carshop_ipn.html',
		'return_url': 'http://localhost:8000/carshop_return.html',
		'cancel_return': 'http://localhost:8000/carshop_cancel.html',
	}
	
	form = PayPalPaymentsForm(initial= paypal_dict)
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

