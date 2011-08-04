# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.models import User
from django.db import models
from django.core.cache import cache
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from carshop.models import Parameter, CountryStateCity
from carshop.product import models as product

class Customer(models.Model): # 客户表
    GENDER_CHOICES = (
        (u'M', u'Male'), (u'F', u'Female'),
    )

    RECEIVE_CHOICES = ((u'Y', u'Yes'), (u'N', u'No'))

    #customer = models.ForeignKey(User, primary_key=True) # 用户id
    user = models.OneToOneField(User, primary_key=True)
    
    customer_name = models.CharField(max_length=60)
    customer_phone_no = models.CharField(max_length=32) # 客户电话
    customer_fax_no = models.CharField(max_length=32, blank=True, null=True) # 客户传真
    customer_gender = models.CharField(max_length=2, choices=GENDER_CHOICES) # 客户性别

    customer_address = models.CharField(max_length=200) # 客户地址
    customer_zip = models.CharField(max_length=10) # 客户邮编

    customer_company = models.CharField(max_length=100) # 客户公司

    customer_is_receive_email = models.CharField(max_length=2, choices=RECEIVE_CHOICES) # 是否接收Email

    customer_status = models.ForeignKey(Parameter, related_name='customer_status', blank=True, null=True) # 客户状态
    customer_level = models.ForeignKey(Parameter, related_name='customer_level', blank=True, null=True) # 客户等级
    customer_integral = models.IntegerField(blank=True, null=True) # 客户积分

    customer_country = models.ForeignKey(CountryStateCity, related_name="country", blank=True, null=True) # 国家
    customer_state = models.ForeignKey(CountryStateCity, related_name="state", blank=True, null=True) # 州/省
    customer_city = models.ForeignKey(CountryStateCity, related_name="city", blank=True, null=True) # 城市

    def __unicode__(self):
        return ("%s" % (self.customer_name))

    class Meta:
        db_table = 'customer'

def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        profile, created = Customer.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


class CustomerAddressHistory(models.Model):
    
    customer = models.ForeignKey(Customer)
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    phone_no = models.CharField(max_length=32, blank=True, null=True) # 客户电话
    fax_no = models.CharField(max_length=32, blank=True, null=True) # 客户传真
    zip = models.CharField(max_length=10) # 客户邮编
    
    country = models.CharField(max_length=32, blank=True)#models.ForeignKey(CountryStateCity, related_name="country_history", blank=True, null=True) # 国家
    state = models.CharField(max_length=32, blank=True)#models.ForeignKey(CountryStateCity, related_name="state_history", blank=True, null=True) # 州/省
    city = models.CharField(max_length=32, blank=True)#models.ForeignKey(CountryStateCity, related_name="city_history", blank=True, null=True) # 城市
    street_address = models.TextField(max_length=500)

    time_add = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return str(self.time_add) + ' ' + self.street_address

    class Meta:
        db_table = 'customer_address_history'

class CustomerMessage(models.Model): # 客户留言表
    customer = models.ForeignKey(Customer, primary_key=True) # 用户id
    message = models.CharField(max_length=2000) # 留言内容
    time_created = models.DateTimeField() # 留言日期
    message_type = models.ForeignKey(Parameter) # 留言类别

    class Meta:
        db_table = "customer_message"


#class CustomerBasket(models.Model): # 购物篮
#    customer = models.ForeignKey(Customer, primary_key=True) # 用户id
#    product = models.ForeignKey(product.Product) # 产品ID
#    product_quantity = models.IntegerField() # 产品数量
#    product_price = models.FloatField() # 产品价格
#    product_final_price = models.FloatField() # 最终价格
#    time_basket_added = models.DateTimeField() # 添加时间

#    class Meta:
#        db_table = "customer_basket"

#class CustomerInfo(models.Model): # 客户账户部分信息
#	customer = models.ForeignKey(Customer) # 客户ID
#	time_last_logon = models.DateTimeField() # 上次登录时间
#	number_logons = models.IntegerField() # 登录次数
#	time_account_created = models.DateTimeField() # 账户创建时间
#	time_account_last_modified = models.DateTimeField() # 上次修改时间

#	class Meta:
#		db_table = "customer_info"

#class CustomerWishList(models.Model): # 客户对产品意见？



	