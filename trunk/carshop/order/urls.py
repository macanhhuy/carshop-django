# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns(
    '',
    (r'^generateOrder$', generate_order),
    (r'^checkout/(?P<orderId>.{36})$', checkout),
    (r'^saveOrder$', save_order),
    (r'^orderStatus.html$', order_status),
)
