# coding: utf-8

from django.contrib import admin
from carshop.product.models import *
from django.db.models.query import QuerySet

class ProductAdmin(admin.ModelAdmin):
	
	fieldsets = (
		(None, {
			'fields':('product_name', 'product_image_url', 'product_manufacturer', 'product_type', 'product_price', 'product_count',)
		}),
		('Advanced options', {
			'fields': ()
		}),
	)
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		from django.db import connection
		cursor = connection.cursor()
		if db_field.name == "product_type":
			kwargs["queryset"] = system.Parameter.objects.extra(where = ["parameter_parent_id in (select p2.id from parameter p2 where p2.parameter_code='product_top_type')",])

			return db_field.formfield(**kwargs)
		
		return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	
	
class ProductAttributeAdmin(admin.ModelAdmin):
	pass
	
class ProductDescriptionAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "language":
			kwargs["queryset"] = system.Parameter.objects.filter(parameter_code='language')
			return db_field.formfield(**kwargs)
		
		return super(ProductDescriptionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	pass
	

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)