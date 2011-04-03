# coding: utf-8
import datetime
from django.contrib import admin
from django.db.models.query import QuerySet
from carshop.product.models import *

class ProductAdmin(admin.ModelAdmin):
	
	fieldsets = (
		(None, {
			'fields':('product_name', 'product_image_url', 'product_manufacturer', 'product_type', 'product_price', 'product_count',)
		}),
		('Advanced options', {
			'fields': ()
		}),
	)
	
	list_display = ('product_name', 'product_manufacturer', 'product_type', 'product_price', 'product_count', )
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		from django.db import connection
		cursor = connection.cursor()
		if db_field.name == "product_type":
			kwargs["queryset"] = Parameter.objects.extra(where = ["parameter_parent_id in (select p2.id from parameter p2 where p2.parameter_code='product_top_type')",])

			return db_field.formfield(**kwargs)
		
		return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
	def save_model(self, request, obj, form, change):
		if not obj.product_added_user_id:
			obj.product_added_user_id = request.user.id
		obj.product_modified_user_id = request.user.id
		
		now = datetime.datetime.now()
		if not obj.time_product_register:
			obj.time_product_register = now
		obj.time_product_modified = now
		obj.save()
	
	
class ProductAttributeAdmin(admin.ModelAdmin):
	pass
	
class ProductDescriptionAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "language":
			kwargs["queryset"] = Parameter.objects.filter(parameter_code='language')
			return db_field.formfield(**kwargs)
		
		return super(ProductDescriptionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	pass
	

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)