# coding: utf-8
import datetime
from django.db import models
from django.core.cache import cache
from django.contrib import admin
from carshop.system import models as system
from carshop.product import models as product

class Customer(models.Model): # 客户表
	GENDER_CHOICES = (
		(u'M', u'Male'),(u'F', u'Female'),
	)

	customer_firstname = models.CharField(max_length=32) # 客户名
	customer_lastname = models.CharField(max_length=32) # 客户名
	customer_email = models.CharField(max_length=30) # 客户email
	customer_phone_no = models.CharField(max_length=32) # 客户电话
	customer_fax_no = models.CharField(max_length=32, blank=True, null=True) # 客户传真
	customer_login = models.CharField(max_length=20) # 客户登陆名
	customer_pass = models.CharField(max_length=50) # 客户密码
	customer_gender = models.CharField(max_length=2, choices=GENDER_CHOICES) # 客户性别
	
	customer_address = models.CharField(max_length=200) # 客户地址
	customer_zip = models.CharField(max_length=10) # 客户邮编
	time_customer_register = models.DateTimeField() # 客户注册时间
	time_customer_updated = models.DateTimeField() # 客户更新时间
	customer_status = models.ForeignKey(system.Parameter, related_name='customer_status', blank=True, null=True) # 客户状态
	customer_level = models.ForeignKey(system.Parameter, related_name='customer_level', blank=True, null=True) # 客户等级
	customer_integral = models.IntegerField(blank=True, null=True) # 客户积分
	
	def __unicode__(self):
		return ("%s %s" % (self.customer_firstname, self.customer_lastname)) 
	
	class Meta:
		db_table = 'customer'





class CustomerMessage(models.Model): # 客户留言表
	customer = models.ForeignKey(Customer) # 客户ID
	message = models.CharField(max_length=2000) # 留言内容
	time_created = models.DateTimeField() # 留言日期
	message_type = models.ForeignKey(system.Parameter) # 留言类别
	
	class Meta:
		db_table = "customer_message"
	
class CustomerBasket(models.Model): # 购物篮
	customer = models.ForeignKey(Customer) # 客户ID
	product = models.ForeignKey(product.Product) # 产品ID
	product_quantity = models.IntegerField() # 产品数量
	product_price = models.FloatField() # 产品价格
	product_final_price = models.FloatField() # 最终价格
	time_basket_added = models.DateTimeField() # 添加时间
	
	class Meta:
		db_table = "customer_basket"
		
class CustomerInfo(models.Model): # 客户账户部分信息
	customer = models.ForeignKey(Customer) # 客户ID
	time_last_logon = models.DateTimeField() # 上次登录时间
	number_logons = models.IntegerField() # 登录次数
	time_account_created = models.DateTimeField() # 账户创建时间
	time_account_last_modified = models.DateTimeField() # 上次修改时间
	
	class Meta:
		db_table = "customer_info"
		
#class CustomerWishList(models.Model): # 客户对产品意见？


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

	