# coding: utf-8

from django.contrib import admin
from carshop.order.models import *


class OrderAdmin(admin.ModelAdmin):
	pass
	
class OrderProductAdmin(admin.ModelAdmin):
	pass
	
class OrderProductDownloadAdmin(admin.ModelAdmin):
	pass
	
class OrderStatusAdmin(admin.ModelAdmin):
	pass
	
class OrderStatusHistoryAdmin(admin.ModelAdmin):
	pass
	
	
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(OrderProductDownload, OrderProductDownloadAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(OrderStatusHistory, OrderStatusHistoryAdmin)