from django.conf.urls.defaults import *
from carshop.customer import views as customer

urlpatterns = patterns('',	
	(r'^money.html$', customer.view_that_asks_for_money),
	(r'^buy.html$', customer.buy_my_item),


)
