# -*- coding: utf-8 -*-

#from django.contrib.auth.models import User
from django.db import models
from carshop.product import models as product
from carshop.models import Parameter, AddressFormat
from carshop.customer.models import Customer
from carshop.db.models import *

class Order(models.Model): # 订单表

    id = UUIDField(primary_key=True, editable=False)
    customer = models.ForeignKey(Customer) # 客户ID
#    customer_name = models.CharField(max_length=64) # 客户名(接收人)
#    customer_company = models.CharField(max_length=64, blank=True, null=True) # 客户公司
#    customer_street_address = models.CharField(max_length=64, blank=True, null=True) # 客户街道地址
#    customer_suburb = models.CharField(max_length=32, blank=True, null=True) # 客户住宅区
#    customer_city = models.CharField(max_length=32, blank=True, null=True) # 客户城市
#    customer_postcode = models.CharField(max_length=10, blank=True, null=True) # 客户邮编
#    customer_state = models.CharField(max_length=32, blank=True, null=True) # 客户所在州
#    customer_country = models.CharField(max_length=32, blank=True, null=True) # 客户国家
#    customer_telephone = models.CharField(max_length=32, blank=True, null=True) # 客户电话
#    customer_email_address = models.CharField(max_length=96, blank=True, null=True) # 客户EMAIL
#    customer_address_format = models.ForeignKey(AddressFormat, related_name='customer_address_format', blank=True, null=True) # 客户地址格式

#    delivery_name = models.CharField(max_length=64, blank=True, null=True) # 送货人名
#    delivery_company = models.CharField(max_length=64, blank=True, null=True) # 送货公司
#    delivery_street_address = models.CharField(max_length=64, blank=True, null=True) # 送货(人/公司？)街道地址
#    delivery_suburb = models.CharField(max_length=32, blank=True, null=True) # 送货(人/公司?)所在区
#    delivery_city = models.CharField(max_length=32, blank=True, null=True) # 送货
#    delivery_postcode = models.CharField(max_length=10, blank=True, null=True) #
#    delivery_state = models.CharField(max_length=32, blank=True, null=True) #
#    delivery_country = models.CharField(max_length=32, blank=True, null=True) #
#    delivery_address_format = models.ForeignKey(AddressFormat, related_name='delivery_address_format', blank=True, null=True) #

    billing_first_name = models.CharField(max_length=30) #
    billing_last_name = models.CharField(max_length=30)#
    billing_company = models.CharField(max_length=64, blank=True, null=True) #
    billing_street_address = models.CharField(max_length=64, blank=True, null=True) #
    billing_suburb = models.CharField(max_length=32, blank=True, null=True) #
    billing_city = models.CharField(max_length=32, blank=True, null=True) #
    billing_postcode = models.CharField(max_length=10, blank=True, null=True) #
    billing_state = models.CharField(max_length=32, blank=True, null=True) #
    billing_country = models.CharField(max_length=32, blank=True, null=True) #
    billing_address_format = models.ForeignKey(AddressFormat, related_name='billing_address_format', blank=True, null=True) #

    payment_method = models.CharField(max_length=128, blank=True, null=True) # 付款方式
    payment_module_code = models.CharField(max_length=32, blank=True, null=True) # ？
    shipping_method = models.CharField(max_length=128, blank=True, null=True) # 购买方式
    shipping_module_code = models.CharField(max_length=32, blank=True, null=True) #

    #coupon_code
    time_purchased = models.DateTimeField(blank=True, null=True) # 购置时间

    order_total_price = models.FloatField() # 总价格
    currency = models.CharField(max_length=3, blank=True, null=True) # ?
    #paypal_ipn
    ip_address = models.CharField(max_length=96) # 下单IP

    class Meta:
        db_table = "order"


class OrderProduct(models.Model): # 订单项表
    order = models.ForeignKey(Order) # 订单ID
    product = models.ForeignKey(product.Product) # 产品ID
    product_name = models.CharField(max_length=64)
    product_quantity = models.IntegerField() # 产品数量
    product_price = models.FloatField() # 产品单价
    product_final_price = models.FloatField() # 产品最终单价
    product_tax = models.FloatField() # 产品税
    onetime_charge = models.FloatField() # 一次性付款数目？

    #product_is_free # 是否免费
    #product_discount = models.ForeignKey(Discount) # 优惠券ID
    product_prid = models.CharField(max_length=36) #

    class Meta:
        db_table = "order_product"

#class OrderProductAttribute(models.Model)

class OrderProductDownload(models.Model): # 订单下载表
    order = models.ForeignKey(Order) # 订单ID
    order_product = models.ForeignKey(OrderProduct) # 订单产品ID
    order_product_filename = models.CharField(max_length=255) # 文件名
    download_maxdays = models.IntegerField() # 最大下载时间(天)
    download_count = models.IntegerField() # 最大下载次数

    class Meta:
        db_table = "order_product_download"

        #product_prid = models


class OrderStatus(models.Model): # 订单状态表
    order = models.ForeignKey(Order) # 订单ID
    customer = models.ForeignKey(Customer, related_name="customer_user") # 客户ID
    order_status = models.ForeignKey(Parameter, related_name='order_status') # 订单状态
    time_update_status = models.DateTimeField() # 状态更新时间
    time_pass = models.DateTimeField() # 确认时间
    order_pass_use = models.ForeignKey(Customer, related_name="manager_user") # 确认管理人
    order_send_type = models.ForeignKey(Parameter, related_name='order_send_type') # 发送状态

    class Meta:
        db_table = "order_status"


class OrderStatusHistory(models.Model): # 订单状态历史表
    order = models.ForeignKey(Order) # 订单ID
    status = models.ForeignKey(Parameter) # 订单状态
    time_added = models.DateTimeField() # 添加时间
    #customer_notified
    comment = models.TextField() # 注释

    class Meta:
        db_table = "order_status_history"

#class OrderTotal(models.Model):

#class Paypal(models.Model):
	
	
	
	
	

	

