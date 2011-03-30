from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.http import HttpResponse
from django.core import serializers
from django.utils.translation import gettext as _

from carshop.system.models import Parameter, CountryStateCity
from carshop.system.context_processors import getLeftNavigate

def index(request):
	return render_to_response('index.html', findTopProduct(), RequestContext(request))#, processors=[getLeftNavigate]))


def findTopProduct():
	return {}
	

def login(request):
	return None

	
def register(request):
	if request.method == 'POST':
		print(request.POST['username'])
	
	else:
		print('cc')
	
def toRegister(request):
	countries = CountryStateCity.objects.extra(where=['parent_id is null',])
	return render_to_response('register.html', {'countries': countries}, RequestContext(request))

	
def findStateOrCity(reqeust, countryId):
	states = CountryStateCity.objects.extra(where=['parent_id=%s',], params=[countryId,])
	format = 'json'
	mimetype = 'application/javascript'
	data = serializers.serialize(format, states)
	return HttpResponse(data,mimetype)
	

	
	