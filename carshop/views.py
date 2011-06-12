# -*- coding:utf-8 -*-

import traceback

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.db import IntegrityError
from django.utils.translation import gettext as _

from carshop.models import Parameter, CountryStateCity, UserManager
from carshop.context_processors import getLeftNavigate
from carshop.forms import RegisterForm
from carshop.utils import NoStyleErrorList
from carshop.product.models import Product

from carshop.customer.models import Customer
from .cart.models import Cart

import Image, ImageDraw, ImageFont, md5, random, cStringIO

def index(request):
#	print('3 ' + request.session['CART-OBJ'].session + ' | ' + request.session.session_key)
    return render_to_response('index.html', findTopProduct(), RequestContext(request))#, processors=[getLeftNavigate]))


def findTopProduct():
    return {'products': Product.objects.all()[0:8]}


def logout_view(request):
#	print('1 ' + request.session['CART-OBJ'].session + ' | ' + request.session.session_key)
    cart = Cart.objects.get_or_create_from_request(request)

    logout(request)

    cart.flush(request)
    #	print('2 ' + request.session['CART-OBJ'].session + ' | ' + request.session.session_key)
    return HttpResponseRedirect('/index.html')


def login_view(request):

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                cart = Cart.objects.get_or_create_from_request(request)
                login(request, user)
                cart.flush(request)
                redirect_url = request.session.get('redirect_url')
                if redirect_url:
                    request.session['redirect_url'] = None
                    return HttpResponseRedirect(redirect_url)
                else:
                    return HttpResponseRedirect('/index.html')
            else:
                return render_to_response('login.html', {'username': username, 'message': 'error'}, RequestContext(request))
        except Exception, e:
            print('22222\n' + e)
            return render_to_response('login.html', {'username': username, 'message': 'error'}, RequestContext(request))
    else:
        return render_to_response('login.html', {}, RequestContext(request))


def login_ajax(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            #if user.is_active:
            login(request, user)
            print('1,' + user.username)
            return HttpResponse('1,' + user.username)
        #else:
        #	return HttpResponse('3,')
        else:
            return HttpResponse('2,')

    return HttpResponse('99,')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, error_class=NoStyleErrorList)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']

                #user = User.objects.create_user(username, email, password)
                #user.first_name = first_name
                #user.last_name = last_name
                #user.is_staff = True
                #user.save()

                address = form.cleaned_data['address']
                zip = form.cleaned_data['zip']

                country = form.cleaned_data['country']
                state = form.cleaned_data['state']
                city = form.cleaned_data['city']

                gender = form.cleaned_data['gender']

                company = form.cleaned_data['company']
                phone_number = form.cleaned_data['phone_number']
                fax_number = form.cleaned_data['fax_number']
                receive_email = form.cleaned_data['receive_email']

                #customer = Customer(username, email, password)
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                
                user.get_profile().customer_name = user.get_full_name()
                user.get_profile().customer_address = address
                user.get_profile().customer_zip = zip

                user.get_profile().customer_country = CountryStateCity.objects.get(id=country)
                user.get_profile().customer_state = CountryStateCity.objects.get(id=state)
                user.get_profile().customer_city = CountryStateCity.objects.get(id=city)

                user.get_profile().customer_gender = gender

                user.get_profile().customer_company = company
                user.get_profile().customer_phone_no = phone_number
                user.get_profile().customer_fax_no = fax_number
                user.get_profile().customer_is_receive_email = receive_email

                user.get_profile().save()
            except Exception, e:
                return render_to_response('error.html', {'e': e, 'traceback_msg': traceback.format_exc()},
                                          RequestContext(request))

            return HttpResponse(u'注册成功!!!')
    else:
        form = RegisterForm(error_class=NoStyleErrorList)

    return render_to_response('register.html', {'form': form}, RequestContext(request))


def toRegister(request):
    form = RegisterForm(initial={'receive_email': 'Y'}, error_class=NoStyleErrorList)
    return render_to_response('register.html', {'form': form}, RequestContext(request))


def findStateOrCity(reqeust, countryId):
    states = CountryStateCity.objects.extra(where=['parent_id=%s', ], params=[countryId, ])
    format = 'json'
    mimetype = 'application/javascript'
    data = serializers.serialize(format, states)
    #print(data)
    return HttpResponse(data, mimetype)


def checkcode(request, time):
    im = Image.new('RGBA', (52, 22), (256, 256, 256, 256))
    draw = ImageDraw.Draw(im)
    rands = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    draw.text((2, 0), str(rands[0]), font=ImageFont.truetype("tahomabd.TTF", random.randrange(12, 18)),
              fill=random.randint(0, 256))
    draw.text((14, 0), str(rands[1]), font=ImageFont.truetype("tahomabd.TTF", random.randrange(12, 18)),
              fill=random.randint(0, 256))
    draw.text((27, 0), str(rands[2]), font=ImageFont.truetype("tahomabd.TTF", random.randrange(12, 18)),
              fill=random.randint(0, 256))
    draw.text((40, 0), str(rands[3]), font=ImageFont.truetype("tahomabd.TTF", random.randrange(12, 18)),
              fill=random.randint(0, 256))
    del draw
    request.session['checkcode'] = rands
    buf = cStringIO.StringIO()
    im.save(buf, 'gif')
    return HttpResponse(buf.getvalue(), 'image/gif')


def paypal_ipn(request):
    return HttpResponse('ipn')


def paypal_return(request):
    print request
    return HttpResponse('return')


def paypal_cancel(request):
    print request
    return HttpResponse('cancel')


def paypal_success(request):
    return HttpResponse('success')
