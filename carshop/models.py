# coding: utf-8
from django.db import models
from django.core.cache import cache
from django.contrib import admin
from django.contrib.auth import models as auth

#class Language(models.Model): # 语言表
#	language_name = models.CharField(max_length=32) # 语言名
#	language_code = models.CharField(max_length=10) # 语言代码
#	language_image = models.CharField(max_length=64, blank=True, null=True) # 语言图片(LOGO)？
#	language_directory = models.CharField(max_length=32, blank=True, null=True) # ？
#	language_sequence = models.IntegerField(blank=True, null=True) # 排序
	
#	def __unicode__(self):
#		return self.language_name;
	
#	class Meta:
#		db_table = "language"

class Parameter(models.Model): # 基础参数表

	VALID_CHOICES = ((1, u' 启用 '), (0, u' 禁用 '), (2, u' 其他 '))

	#id = models.AutoField('id', primary_key=True)
	parameter_code = models.CharField(max_length=40) # 参数代码
	parameter_parent = models.ForeignKey('self', related_name='parent', blank=True, null=True) # 父
	parameter_display_name = models.CharField(max_length=40) # 参数显示名
	parameter_value = models.CharField(max_length=40, blank=True, null=True) # 参数值
	parameter_extension_value = models.CharField(max_length=40, blank=True, null=True) # 备用值
	parameter_desc = models.TextField(max_length=50, blank=True, null=True) # 参数描述
	parameter_sequence = models.IntegerField() # 参数顺序
	parameter_is_valid = models.IntegerField(default=1, choices=VALID_CHOICES) # 参数是否有效
	time_parameter_created = models.DateTimeField() # 创建时间
	parameter_language = models.ForeignKey('self', 'id', related_name='language', blank=True, null=True) # 语言
	
	def __unicode__(self):
		return self.parameter_display_name
	
	class Meta:
		db_table = "parameter"
		

class Bulletin(models.Model): # 公告表
	
	bulletin_title = models.CharField(max_length=100) # 公告标题
	bulletin_body = models.CharField(max_length=2000) # 公告内容
	time_bulletin_created = models.DateTimeField() # 公告添加时间
	time_bulletin_updated = models.DateTimeField() # 公告更新时间
	bulletin_add_use = models.ForeignKey(auth.User) # 公告添加管理员
	bulletin_point = models.IntegerField() # 点击数/浏览量
	bulletin_sequence =models.IntegerField() # 公告顺序
	bulletin_is_valid = models.IntegerField(default=1) # 是否有效
	
	class Meta:
		db_table = "bulletin"

class AddressFormat(models.Model): # 地址格式表
	format = models.CharField(max_length=128) # 地址格式
	summary = models.CharField(max_length=48) # 地址摘要 ？
	
	class Meta:
		db_table = "address_format"
	
	

class CountryStateCity(models.Model): # 国家、州、省、城市 表
	
	VALID_CHOICES = ((1, u' 启用 '), (0, u' 禁用 '), (2, u' 其他 '))

	name = models.CharField(max_length=64) # 名
	country_iso_code_2 = models.CharField(max_length=2, blank=True, null=True) # 2位ISO代码
	country_iso_code_3 = models.CharField(max_length=3, blank=True, null=True) # 3位ISO代码
	parent = models.ForeignKey('self', related_name='country_state_city_parent', blank=True, null=True)
	address_format = models.ForeignKey(AddressFormat, blank=True, null=True) # 地址格式
	sequence =models.IntegerField() # 顺序
	is_valid = models.IntegerField(default=1, choices=VALID_CHOICES) # 是否有效
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "country_state_city"

	
class EmailArchive(models.Model): # 邮件存档表
	email_to_name = models.CharField(max_length=96) # 接收人名
	email_to_address = models.CharField(max_length=96) # 接收人EMAIL地址
	email_from_name = models.CharField(max_length=96) # 发送人名
	email_from_address = models.CharField(max_length=96) # 发送人EMAIL地址
	email_subject = models.CharField(max_length=255) # 邮件主题
	email_html = models.TextField(blank=True, null=True) # 邮件HTML内容
	email_text = models.TextField() # 邮件内容
	time_send = models.DateTimeField() # 发送时间
	
	class Meta:
		db_table = "email_archive"

	
class LayoutBox(models.Model): # 模板配置表
	layout_name = models.CharField(max_length=64) # 模板名
	layout_template = models.CharField(max_length=64) # 模板文件名
	layout_template_path = models.CharField(max_length=255) # 模板路径
	layout_status = models.ForeignKey(Parameter) # 模板状态
	
	class Meta:
		db_table = "layout_box"
	
	
	
#class EzPage(models.Model): # ez page
	#languages_id
#	pages_title = models.CharField(max_length=64) # 
#	alt_url = models.CharField(max_length=255) # 
#	alt_url_external = models.CharFiels(max_length=255) # 
#	page_template = models.CharField(max_length=255) # 

#	class Meta:
#		db_table = 


#class Discount(models.Model)

class MetaTagCategoryDescription(models.Model): # 类别meta标签描述表
	language = models.ForeignKey(Parameter) # 标签对应语言
	metatag_title = models.CharField(max_length=255) # 标签标题
	metatag_keyword = models.TextField() # 标签关键字
	metatag_desc = models.TextField(blank=True, null=True) # 标签描述
	
	class Meta:
		db_table = "mattag_category_description"
	
class MetaTagProductDescription(models.Model): # 产品meta标签描述表
	language = models.ForeignKey(Parameter) # 标签名
	metatag_title = models.CharField(max_length=255) # 标签标题
	metatag_keyword = models.TextField() # 标签关键字
	metatag_desc = models.TextField(blank=True, null=True) # 标签描述
	
	class Meta:
		db_table = "mattag_product_description"

#class CustomerInline(admin.TabularInline):
#	model = customer.Customer
#	fk_name = "customer_status"

	


def cache_load():
	cache.set('customer_status_code', Parameter.objects.filter(parameter_code='customer_status_code'))
	
#cache_load()
