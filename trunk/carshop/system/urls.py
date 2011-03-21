from django.conf.urls.defaults import *
from django.views.generic import list_detail
from carshop.system import views as system


urlpatterns = patterns('',	
	(r'^left_navi.html$', list_detail.object_list, system.getLeftNavi()),


)
