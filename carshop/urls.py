# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin

from rollyourown.seo.admin import register_seo_admin
from .seo import CarShopMetadata

import settings

from .views import *

admin.autodiscover()
register_seo_admin(admin.site, CarShopMetadata)

urlpatterns = patterns(
    '',
    # Example:
    # (r'^carshop/', include('carshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    (r'^admin/', include(admin.site.urls)),
    (r'^search$', search),

    (r'^customer/', include('carshop.customer.urls')),
    (r'^product/', include('carshop.product.urls')),
    (r'^cart/', include('carshop.cart.urls')),
    (r'^order/', include('carshop.order.urls')),
    (r'^brand/', include('carshop.brand.urls')),
    
    (r'^index.html$', index),
    (r'^$', index),

    (r'^login/(?P<redirect>.*)$', login_view),
    #(r'^login$', 'carshop.views.login_ajax'),
    (r'^logout$', logout_view),
    (r'^register$', register),
    (r'^toRegister$', toRegister),
    (r'^findStateOrCity/(?P<countryId>\d{1,6})$', find_state_or_city),

    #(r'^checkcode/(?P<time>\d{13})$', checkcode),

    #########################################
    #
    #
    #########################################
    #(r'^paypal_success$', paypal_success),
    #(r'^paypal_ipn$', paypal_ipn),
    #(r'^paypal_return$', paypal_return),
    #(r'^paypal_cancel$', paypal_cancel),


)
