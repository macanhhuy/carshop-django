# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from carshop.product.views import *

urlpatterns = patterns(
    '',
    (r'^(?P<productTypeId>\d{1,3}).html$', findProductTypeById),
#    (r'^(?P<productTypeId>\d{1,3})/(?P<productId>\d{1,3}).html$', findProductById),
    (r'^detail(?P<productId>\d{1,3}).html', findProductById),
    
    (r'^car(?P<carId>\d{1,4}).html', findProductByCarId),

)