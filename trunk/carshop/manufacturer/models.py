# coding: utf-8
from django.db import models
from django.contrib import admin

class Manufacturer(models.Model):  # 制造商标
	manufacturer_name = models.CharField(u'制造商名', max_length=50) # 制造商名
	date_created = models.DateField() # 创立时间
	time_added = models.DateTimeField() # 注册时间/添加时间
	time_modified = models.DateTimeField() # 最后修改时间
	manufacturer_image = models.CharField(max_length=255, blank=True, null=True) # 制造商图片(LOGO)
	manufacturer_desc = models.CharField(max_length=2000, blank=True, null=True) # 描述
	
	class Meta:
		db_table = 'manufacturer'

		
		
		
		
class ManufacturerAdmin(admin.ModelAdmin):
	
	list_display = ('manufacturer_name', 'iso_date_created',)
	
	def iso_date_created(self, obj):
		return obj.date_created.isoformat()
	iso_date_created.short_description = 'Date Created'
	
admin.site.register(Manufacturer, ManufacturerAdmin)
