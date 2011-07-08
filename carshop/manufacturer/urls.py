# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns(
    '',
    (r'^(?P<productTypeId>\d{1,3}).html$', findProductTypeById),


)