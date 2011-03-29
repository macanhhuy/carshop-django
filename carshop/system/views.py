from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.http import HttpResponse
from django.core import serializers
from django.utils.translation import gettext as _

from carshop.system.models import Parameter
from carshop.system.context_processors import getLeftNavigate

def index(request):
	return render_to_response('index.html', findTopProduct(), RequestContext(request))#, processors=[getLeftNavigate]))


def findTopProduct():
	return {}
	

def login(request):
	return None

	
def toRegister(request):
	countries = Parameter.objects.filter(parameter_code='country_code')
	return render_to_response('register.html', {'countries': countries}, RequestContext(request))

	
def findState(reqeust, countryIso):
	states = Parameter.objects.extra(where=['parameter_parent_id=(select p1.id from parameter as p1 where p1.parameter_value=%s) order by parameter_sequence',], params=[countryIso,])
	format = 'json'
	mimetype = 'application/javascript'
	data = serializers.serialize(format, states)
	print(data)
	return HttpResponse(data,mimetype)
	
	