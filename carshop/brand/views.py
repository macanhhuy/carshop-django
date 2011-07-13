# -*- coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *


def allBrand(request):
    brands = list(Brand.objects.raw('select brands.id, brands.name, brands.url_name from brands order by brands.name'))
    return render_to_response('allBrand.html', {'brands': brands}, RequestContext(request))
