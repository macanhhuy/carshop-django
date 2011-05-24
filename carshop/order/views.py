# -*- coding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from models import *

def check_order(request):
    if not request.user.is_authenticated():
        request.session['redirect_url'] = '/cart/cart.html'#request.path
        return HttpResponseRedirect('/login.html')
    
    return render_to_response('check_order.html', {}, RequestContext(request))