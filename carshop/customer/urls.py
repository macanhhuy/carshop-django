from django.conf.urls.defaults import *
from carshop.customer.views import *

urlpatterns = patterns('',	
	(r'^money.html$', view_that_asks_for_money),
	(r'^buy.html$', buy_my_item),


)
