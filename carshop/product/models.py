# coding: utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth import models as auth
from carshop.manufacturer import models as manufacturer
from carshop.system import models as system
	
	
class Product(models.Model): #
	product_name = models.CharField(max_length=100) # 名称
	product_model = models.CharField(max_length=62, blank=True, null=True)
	product_image_url = models.CharField(max_length=100, blank=True, null=True) # 图片地址
	product_manufacturer = models.ForeignKey(manufacturer.Manufacturer) # 制造商
	
	product_type = models.ForeignKey(system.Parameter, related_name='product_type') # 物品类别
	product_price = models.FloatField()	# 价格
	product_order_desc = models.CharField(max_length=1000) # 订购说明
	product_count = models.IntegerField() # 库存
	time_product_register = models.DateTimeField() # 上架时间
	time_product_modified = models.DateTimeField() # 修改时间
	time_product_available = models.DateTimeField(blank=True, null=True) # 到期时间?
	product_added_user = models.ForeignKey(auth.User, related_name='product_added_user') # 添加人员
	product_modified_user = models.ForeignKey(auth.User, related_name='product_modified_user') # 修改人员
	product_status = models.ForeignKey(system.Parameter, related_name='product_status', blank=True, null=True) # 产品状态
	product_weight = models.FloatField(blank=True, null=True) # 产品重
	product_tax = models.ForeignKey(system.Parameter, related_name='product_tax', blank=True, null=True) # 税 外键
	product_quantity_order_min = models.IntegerField(default=1) # 单次购买最小数量
	product_quantity_order_max = models.IntegerField(default=999) # 单次购买最大数量
	product_sequence = models.IntegerField(blank=True, null=True) # 排序
	
	metatag_title_status = models.IntegerField(blank=True, null=True) # ?
	metatag_product_name_status = models.IntegerField(blank=True, null=True) # ?
	metatag_model_status = models.IntegerField(blank=True, null=True) # ?
	metatag_price_status = models.IntegerField(blank=True, null=True) # ?
	metatag_title_tagline_status = models.IntegerField(blank=True, null=True) # ?
	
	class Meta:
		db_table = 'product'
		
class ProductAttribute(models.Model): # 产品属性表
	product = models.ForeignKey(Product) # 产品ID
	
	class Meta:
		db_table = 'product_attribute'
	

class ProductDescription(models.Model): # 产品描述表
	product = models.ForeignKey(Product) # 产品ID
	language = models.ForeignKey(system.Language) # 语言ID
	product_name = models.CharField(max_length=64) # 产品名
	product_desc = models.TextField(blank=True, null=True) # 产品描述
	product_url = models.CharField(max_length=255, blank=True, null=True) # 产品URL
	product_viewed = models.IntegerField(blank=True, null=True) # ？
	
	class Meta:
		db_table = 'product_description'

#class Coupon(models.Model): # 优惠券

	
	
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
			kwargs["queryset"] = system.Parameter.objects.filter(parameter_parent=system.Parameter.objects.get(parameter_code='product_menu_root').id)
			return db_field.formfield(**kwargs)
		
		return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	
	
	
class ProductAttributeAdmin(admin.ModelAdmin):
	pass
	
class ProductDescriptionAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)



