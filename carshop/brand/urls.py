# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns(
    '',
    (r'^all.html$', all),
    (r'^brand-(?P<brandName>.*).html', brand),

)
