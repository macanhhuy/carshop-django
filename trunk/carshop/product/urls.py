# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns(
    '',
    #(r'^(?P<productTypeId>\d{1,3}).html$', findProductTypeById),
#    (r'^(?P<productTypeId>\d{1,3})/(?P<productId>\d{1,3}).html$', findProductById),
    (r'^detail(?P<productId>\d{1,3}).html', findProductById),
    
    (r'^car(?P<carId>\d{1,4}).html', findProductByCarId),
    (r'^car/(?P<manufacturerName>[\w|\s]{1,10}).html', findCartByMaker),
    
    (r'^all.html$', all),
    (r'^all-(?P<pageIndex>\d{0,2}).html$', all),

    (r'^(?P<name>\S{5,20}).html', findProductByName)

)
