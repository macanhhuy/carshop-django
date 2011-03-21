# coding: utf-8

from django.contrib import admin
from carshop.manufacturer.models import *

class ManufacturerAdmin(admin.ModelAdmin):
	
	list_display = ('manufacturer_name', 'iso_date_created',)
	
	def iso_date_created(self, obj):
		return obj.date_created.isoformat()
	iso_date_created.short_description = 'Date Created'
	
admin.site.register(Manufacturer, ManufacturerAdmin)

