from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.utils.translation import gettext as _

from carshop.system.models import Parameter
from carshop.system.context_processors import getLeftNavigate

def index(request):
	return render_to_response('index.html', {}, RequestContext(request))#, processors=[getLeftNavigate]))

