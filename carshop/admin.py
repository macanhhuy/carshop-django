# coding: utf-8

from django.contrib import admin
from carshop.models import *

class ParameterAdmin(admin.ModelAdmin):
	#inlines = [
	#	CustomerInline,
	#]
	
	search_fields = ['parameter_code']
	
	list_display = ('parameter_code', 'parameter_display_name', 'parameter_value', 'parameter_sequence', 'is_valid', 'iso_time_created',)
	
	def is_valid(self, obj):
		if obj.parameter_is_valid == 1:
			return u'启用'
		elif obj.parameter_is_valid == 0:
			return u'禁用'
		elif obj.parameter_is_valid == 2:
			return u'其他'
		else:
			return ''
	is_valid.short_description = 'Is Valid'
	
	def iso_time_created(self, obj):
		return obj.time_parameter_created.isoformat(' ')
	iso_time_created.short_description = 'Time Created'
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "parameter_language":
			kwargs["queryset"] = Parameter.objects.filter(parameter_code='language')
			return db_field.formfield(**kwargs)
		
		return super(ParameterAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	
class BulletinAdmin(admin.ModelAdmin):
	pass
	
class AddressFormatAdmin(admin.ModelAdmin):
	pass
	
#class CountryAdmin(admin.ModelAdmin):
#	pass
	
class EmailArchiveAdmin(admin.ModelAdmin):
	pass
	
class LayoutBoxAdmin(admin.ModelAdmin):
	pass
	
#class LanguageAdmin(admin.ModelAdmin):
#	pass
	
class MetaTagCategoryDescriptionAdmin(admin.ModelAdmin):
	pass
	
class MetaTagProductDescriptionAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(AddressFormat, AddressFormatAdmin)
#admin.site.register(Country, CountryAdmin)
admin.site.register(EmailArchive, EmailArchiveAdmin)
admin.site.register(LayoutBox, LayoutBoxAdmin)
#admin.site.register(Language, LanguageAdmin)
admin.site.register(MetaTagCategoryDescription, MetaTagCategoryDescriptionAdmin)
admin.site.register(MetaTagProductDescription, MetaTagProductDescriptionAdmin)