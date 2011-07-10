# -*- coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *


def all(request):
    manufacturers = list(Manufacturer.objects.raw('select manufacturer.id, manufacturer.manufacturer_name from manufacturer order by manufacturer.manufacturer_name'))
    return render_to_response('all.html', {'manufacturers': manufacturers}, RequestContext(request))
