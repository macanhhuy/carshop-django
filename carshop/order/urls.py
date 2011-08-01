# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns(
    '',
    (r'^generateOrder$', generate_order),
    (r'^checkout/(?P<orderId>.{36})$', checkout),
    (r'^checkout$', save_order),
    (r'^orderStatus.html$', order_status),
    (r'^paypalReturn$', paypal_return),

    (r'^changeQty/(?P<orderId>.{36})/(?P<orderProductId>\d{1,3})/(?P<count>-?\d{1,2})', change_qty),
)
