# coding: utf-8
import datetime
from django.contrib import admin
from carshop.manufacturer.models import *

class ManufacturerAdmin(admin.ModelAdmin):
	
	fieldsets = (
		(None, {
            'fields':('manufacturer_name', 'date_created',)
		}),
        ('Advanced options', {
            'fields': ('manufacturer_image', 'manufacturer_desc', )
        }),
	)
	
	list_display = ('manufacturer_name', 'iso_date_created', 'iso_time_added', 'iso_time_modified')
	
	def iso_date_created(self, obj):
		return obj.date_created.isoformat()
	iso_date_created.short_description = 'Date Created'
	
	def iso_time_added(self, obj):
		return obj.time_added.isoformat(' ')
	iso_time_added.short_description = 'Added Time'
	
	def iso_time_modified(self, obj):
		return obj.time_modified.isoformat(' ')
	iso_time_modified.short_description = 'Modified Time'
	
	def save_model(self, request, obj, form, change):
		if obj.time_added == None:
			obj.time_added = datetime.datetime.now()
		obj.time_modified = datetime.datetime.now()
		obj.save()
	
admin.site.register(Manufacturer, ManufacturerAdmin)

