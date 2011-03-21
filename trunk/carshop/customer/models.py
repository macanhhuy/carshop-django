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



	