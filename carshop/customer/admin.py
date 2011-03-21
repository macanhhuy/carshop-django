# coding: utf-8

from django.contrib import admin
from carshop.customer.models import *



class CustomerAdmin(admin.ModelAdmin):
	date_hierarchy = 'time_customer_register'
	fieldsets = (
		(None, {
            'fields':('customer_firstname', 'customer_lastname', 'customer_email', 'customer_phone_no', 'customer_login', 'customer_pass', 'customer_gender', 'customer_address', 'customer_zip',)
		}),
        ('Advanced options', {
            'fields': ('customer_fax_no', 'customer_status', 'customer_level', 'customer_integral', )
        }),
	)
	
	list_display = ('full_name', 'customer_email', 'customer_phone_no', 'customer_address', 'customer_login', 'status_value', 'iso_register_time', 'iso_update_time', 'logon_number')
	
	#list_filter = ('customer_status',)
	
	search_fields = ['customer_firstname', 'customer_lastname', 'customer_email', 'customer_phone_no', 'customer_login', 'customer_pass', 'customer_gender', 'customer_address', 'customer_zip',]
	
	#date_hierarchy = 'time_customer_register'
	
	def logon_number(self, obj):
		return CustomerInfo.objects.get(id=obj.id).number_logons
	
	
	def full_name(self, obj):
		return ("%s %s" % (obj.customer_firstname, obj.customer_lastname)).upper()
	full_name.short_description = 'Name'
	full_name.admin_order_field = 'customer_firstname'
	def iso_register_time(self, obj):
		return obj.time_customer_register.isoformat(' ')
	iso_register_time.short_description = 'Time Register'
	iso_register_time.admin_order_field = 'time_customer_register'
	def iso_update_time(self, obj):
		return obj.time_customer_updated.isoformat(' ')
	iso_update_time.short_description = 'Timer Update'
	iso_update_time.admin_order_field = 'time_customer_updated'
	
	def status_value(self, obj):
		return obj.customer_status.parameter_display_name

	#def filter_customer_status(self, obj):
	#	return system.Parameter.objects.get(id=obj.customer_status).parameter_display_name
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "customer_status":
			if not cache.get('customer_status_code'):
				cache.set('customer_status_code', system.Parameter.objects.filter(parameter_code='customer_status_code'))
				print('load cache: customer_status_code ')
			kwargs["queryset"] = cache.get('customer_status_code')
			return db_field.formfield(**kwargs)
		if db_field.name == 'customer_level':
			kwargs["queryset"] = system.Parameter.objects.filter(parameter_code='customer_level_code')
			return db_field.formfield(**kwargs)
		return super(CustomerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	def save_model(self, request, obj, form, change):
		if obj.time_customer_register == None:
			obj.time_customer_register = datetime.datetime.now()
		obj.time_customer_updated = datetime.datetime.now()
		obj.save()

class CustomerMessageAdmin(admin.ModelAdmin):
	pass

class CustomerBasketAdmin(admin.ModelAdmin):
	pass
	
class CustomerInfoAdmin(admin.ModelAdmin):

	list_display = ('customer', 'iso_time_last_logon', 'number_logons', 'iso_time_created', 'iso_time_modified',)
	
	def iso_time_last_logon(self, obj):
		return obj.time_last_logon.isoformat(' ')
	
	def iso_time_created(self, obj):
		return obj.time_account_created.isoformat(' ')
	
	def iso_time_modified(self, obj):
		return obj.time_account_last_modified.isoformat(' ')
	
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerMessage, CustomerMessageAdmin)
admin.site.register(CustomerBasket, CustomerBasketAdmin)
admin.site.register(CustomerInfo, CustomerInfoAdmin)