# coding: utf-8

from django.contrib import admin
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
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "product_type":
			kwargs["queryset"] = system.Parameter.objects.filter(parameter_parent=system.Parameter.objects.get(parameter_code='product_type_root').id)
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