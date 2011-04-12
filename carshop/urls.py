from django.conf.urls.defaults import *
from django.contrib import admin

from rollyourown.seo.admin import register_seo_admin
from carshop.seo import CarShopMetadata

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
register_seo_admin(admin.site, CarShopMetadata)

urlpatterns = patterns('',
    # Example:
    # (r'^carshop/', include('carshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': './medias'}),
    (r'^admin/', include(admin.site.urls)),
	(r'^customer/', include('carshop.customer.urls')),
	(r'^product/', include('carshop.product.urls')),
	
	
	(r'^index.html$', 'carshop.views.index'),
	(r'^$', 'carshop.views.index'),

	(r'^login$', 'carshop.views.login_view'),
	(r'^logout$', 'carshop.views.logout_view'),
	(r'^register$', 'carshop.views.register'),
	(r'^toRegister$', 'carshop.views.toRegister'),
	(r'^findStateOrCity/(?P<countryId>\d{1,6})$', 'carshop.views.findStateOrCity'),
	
	(r'^checkcode.gif', 'carshop.views.checkcode'),
	
	(r'^allCar.html', 'carshop.product.views.allCar'),
	
	
	#(r'^index$', 'carshop.system.views.index'),
	
)
