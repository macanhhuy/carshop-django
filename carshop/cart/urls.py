# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from carshop.cart.views import *

urlpatterns = patterns('',	
	(r'^(?P<productId>\d{1,3})/(?P<quantity>\d{1,3})$', add_cart),
	(r'^cartView$', cart_view),
	
)