# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import *


def all(request):
    #brands = list(Brand.objects.raw('select brands.id, brands.name, brands.url_name from brands order by brands.name'))
    brands = Brand.objects.all()
    return render_to_response('allBrand.html', {'brands': brands}, RequestContext(request))

def brand(request, brandName):
    return HttpResponse(brandName)