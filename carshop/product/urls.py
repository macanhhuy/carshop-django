from django.conf.urls.defaults import *
from carshop.product.views import *

urlpatterns = patterns('',	
	(r'^(?P<productTypeId>\d{1,3}).html$', findProductById),
	(r'^(?P<productTypeId>\d{1,3})/(?P<productSubTypeId>\d{2,4}).html$', findProductById),
	
	(r'^car/(?P<carId>\d{1,4}).html', findProductByCarId),
	
)