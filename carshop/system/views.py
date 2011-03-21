from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.utils.translation import gettext as _

from carshop.system.models import Parameter
from carshop.system.context_processors import getLeftNavigate

def index(request):
	#print('********index**********\n' + request.LANGUAGE_CODE + '\n***********************')
	return render_to_response('index.html', {}, RequestContext(request))#, processors=[getLeftNavigate]))

#def getLeftNavi():
#	left_navi = cache.get('left_navi')
#	if left_navi == None:
#		first_menu = Parameter.objects.filter('parameter_code'='product_first_menu')
#		for item in first_menu:
#			second_menu = Parameter.objects.filter('parameter_code'='')
#		left_navi = {'firstMenu': Parameter.objects.filter('parameter_code'='product_first_menu')}
		
		
#	cache.set('left_navi', left_navi)