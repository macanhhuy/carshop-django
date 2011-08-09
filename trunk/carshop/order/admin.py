# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', )

    list_filter = ('time_purchased', 'customer')

    list_per_page = 20

    search_fields = ('id', 'billing_first_name', 'billing_last_name', )

    def full_name(self, obj):
        return obj.billing_first_name + ' ' + obj.billing_last_name


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