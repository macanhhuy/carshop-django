# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from carshop.order.views import *

urlpatterns = patterns(
    '',
    (r'^generateOrder$', generate_order),
    (r'^checkout/$', checkout),
    (r'^saveOrder$', save_order),

)
