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
	
	
	
	(r'^index.html$', 'carshop.system.views.index'),
	(r'^$', 'carshop.system.views.index'),
	
	
	#(r'^index$', 'carshop.system.views.index'),
	
)
