from django.conf.urls.defaults import *
from carshop.product.views import *

urlpatterns = patterns('',	
	(r'^(?P<productTypeId>\d{1,5}).html$', customSeatCovers),
	(r'^(?P<productTypeId>\d{1,5})/(?P<productSubTypeId>\d{2,5}).html$', customSeatCovers),
	
)