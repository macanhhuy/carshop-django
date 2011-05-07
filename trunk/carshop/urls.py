# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin

from rollyourown.seo.admin import register_seo_admin
from carshop.seo import CarShopMetadata

import settings

admin.autodiscover()
register_seo_admin(admin.site, CarShopMetadata)

urlpatterns = patterns('',
    # Example:
    # (r'^carshop/', include('carshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    (r'^admin/', include(admin.site.urls)),
	(r'^customer/', include('carshop.customer.urls')),
	(r'^product/', include('carshop.product.urls')),
	(r'^cart/', include('carshop.cart.urls')),
	
	
	(r'^index.html$', 'carshop.views.index'),
	(r'^$', 'carshop.views.index'),

	(r'^login/$', 'carshop.views.login'),
	#(r'^login$', 'carshop.views.login_view'),
	(r'^logout$', 'carshop.views.logout_view'),
	(r'^register$', 'carshop.views.register'),
	(r'^toRegister$', 'carshop.views.toRegister'),
	(r'^findStateOrCity/(?P<countryId>\d{1,6})$', 'carshop.views.findStateOrCity'),
	
	(r'^checkcode/(?P<time>\d{13})$', 'carshop.views.checkcode'),
	
	(r'^allCar.html$', 'carshop.product.views.allCar'),
	(r'^allProduct.html$', 'carshop.product.views.allProduct'),
	
	#(r'^index$', 'carshop.system.views.index'),

	
	#########################################
	#
	#
	#########################################
	(r'^paypal_ipn$', 'carshop.views.paypal_ipn'),
	(r'^paypal_return$', 'carshop.views.paypal_return'),
	(r'^paypal_cancel$', 'carshop.views.paypal_cancel'),
	
	
)
