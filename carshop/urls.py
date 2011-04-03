from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

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
	
	
	(r'^index.html$', 'carshop.system.views.index'),
	(r'^$', 'carshop.system.views.index'),

	(r'^login$', 'carshop.system.views.login_view'),
	(r'^logout$', 'carshop.system.views.logout_view'),
	(r'^register$', 'carshop.system.views.register'),
	(r'^toRegister$', 'carshop.system.views.toRegister'),
	(r'^findStateOrCity/(?P<countryId>\d{1,6})$', 'carshop.system.views.findStateOrCity'),
	
	
	(r'^allManufacturer.html', 'carshop.manufacturer.views.allManufacturer'),
	
	
	#(r'^index$', 'carshop.system.views.index'),
	
)
