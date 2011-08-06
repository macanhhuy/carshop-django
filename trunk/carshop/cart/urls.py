# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from carshop.cart.views import *

urlpatterns = patterns(
    '',
    (r'^(?P<productId>\d{1,3})/(?P<quantity>\d{1,3})$', add_item),
    (r'^changeItemQty/(?P<productId>\d{1,3})/(?P<quantity>-?\d{1,2})$', change_item_qty),

    (r'^remove/(?P<itemId>\d{1,3})$', remove_item),
    (r'^clean$', clean_cart),
    (r'^cart.html$', cart_view),



)
