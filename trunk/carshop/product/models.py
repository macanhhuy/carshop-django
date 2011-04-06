# coding: utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth import models as auth
from carshop.manufacturer import models as manufacturer
from carshop.models import Parameter
	
	
class Product(models.Model): #
	product_name = models.CharField(max_length=100) # 名称
	product_model = models.CharField(max_length=62, blank=True, null=True)
	product_image_url = models.CharField(max_length=100, blank=True, null=True) # 图片地址
	product_manufacturer = models.ForeignKey(manufacturer.Manufacturer, blank=True, null=True) # 制造商
	
	product_type = models.ForeignKey(Parameter, related_name='product_type') # 物品类别
	product_price = models.FloatField()	# 价格
	product_order_desc = models.CharField(max_length=1000) # 订购说明
	product_count = models.IntegerField() # 库存
	time_product_register = models.DateTimeField() # 上架时间
	time_product_modified = models.DateTimeField() # 修改时间
	time_product_available = models.DateTimeField(blank=True, null=True) # 到期时间?
	product_added_user = models.ForeignKey(auth.User, related_name='product_added_user') # 添加人员
	product_modified_user = models.ForeignKey(auth.User, related_name='product_modified_user') # 修改人员
	product_status = models.ForeignKey(Parameter, related_name='product_status', blank=True, null=True) # 产品状态
	product_weight = models.FloatField(blank=True, null=True) # 产品重
	product_tax = models.ForeignKey(Parameter, related_name='product_tax', blank=True, null=True) # 税 外键
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
	language = models.ForeignKey(Parameter) # 语言ID
	product_name = models.CharField(max_length=64) # 产品名
	product_desc = models.TextField(blank=True, null=True) # 产品描述
	product_url = models.CharField(max_length=255, blank=True, null=True) # 产品URL
	product_viewed = models.IntegerField(blank=True, null=True) # ？
	
	class Meta:
		db_table = 'product_description'


#class Coupon(models.Model): # 优惠券


class CarManufacturer(models.Model):  # 汽车制造商
	name = models.CharField(u'', max_length=50) # 名字
	time_added = models.DateTimeField() # 注册时间/添加时间
	time_modified = models.DateTimeField() # 最后修改时间
	manufacturer_image = models.CharField(max_length=255, blank=True, null=True) # 制造商图片(LOGO)
	manufacturer_desc = models.CharField(max_length=2000, blank=True, null=True) # 描述
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'car_manufacturer'


#class Product

