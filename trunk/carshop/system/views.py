from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.http import HttpResponse
from django.core import serializers
from django.utils.translation import gettext as _

from carshop.system.models import Parameter, CountryStateCity
from carshop.system.context_processors import getLeftNavigate
from carshop.system.forms import RegisterForm
from carshop.system.utils import NoStyleErrorList

def index(request):
	return render_to_response('index.html', findTopProduct(), RequestContext(request))#, processors=[getLeftNavigate]))


def findTopProduct():
	return {}
	

def login(request):
	return None

	
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST, error_class=NoStyleErrorList)
		if form.is_valid():
			return HttpResponse(form.cleaned_data['username'])
	else:
		form = RegisterForm(error_class=NoStyleErrorList)

	countries = CountryStateCity.objects.extra(where=['parent_id is null',])
	return render_to_response('register.html', {'form': form, 'countries': countries}, RequestContext(request))
	
def toRegister(request):
	
	form = RegisterForm(error_class=NoStyleErrorList)
	
	countries = CountryStateCity.objects.extra(where=['parent_id is null',])
	return render_to_response('register.html', {'form': form, 'countries': countries}, RequestContext(request))

	
def findStateOrCity(reqeust, countryId):
	states = CountryStateCity.objects.extra(where=['parent_id=%s',], params=[countryId,])
	format = 'json'
	mimetype = 'application/javascript'
	data = serializers.serialize(format, states)
	print(data)
	return HttpResponse(data,mimetype)
	

	
	