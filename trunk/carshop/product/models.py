# -*- coding: utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from ..manufacturer.models import CarModels
from ..models import Parameter


class ProductBrand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)


class ProductBrandAttribute(models.Model):
    product_brand = models.ForeignKey(ProductBrand)
    image = models.ImageField(upload_to='brand_images', blank=True, null=True)


class Product(models.Model): #
    product_name = models.CharField(u'产品名字', max_length=100) # 名称
    product_model = models.CharField(max_length=62, blank=True, null=True)
    product_image = models.ImageField(u'产品图片', upload_to='product_images', blank=True, null=True)
    car_model = models.ForeignKey(CarModels, blank=True, null=True) # 所属
    product_desc = models.TextField(u'产品描述', blank=True, null=True) # 产品描述

    product_category = models.ForeignKey(Parameter, related_name='product_category') # 物品类别
    product_price = models.DecimalField(max_digits=18, decimal_places=2) # 价格
    product_order_desc = models.CharField(u'订购说明', max_length=1000, blank=True, null=True) # 订购说明
    product_count = models.IntegerField() # 库存
    time_product_register = models.DateTimeField() # 上架时间
    time_product_modified = models.DateTimeField() # 修改时间
    time_product_available = models.DateTimeField(u'到期时间', blank=True, null=True) # 到期时间?
    product_added_user = models.ForeignKey(User, related_name='product_added_user') # 添加人员
    product_modified_user = models.ForeignKey(User, related_name='product_modified_user') # 修改人员
    product_status = models.ForeignKey(Parameter, related_name='product_status', blank=True, null=True) # 产品状态
    product_weight = models.FloatField(u'产品重', blank=True, null=True) # 产品重
    product_tax = models.ForeignKey(Parameter, related_name='product_tax', blank=True, null=True) # 税 外键
    product_quantity_order_min = models.IntegerField(u'单次购买下限', default=1) # 单次购买最小数量
    product_quantity_order_max = models.IntegerField(u'单次购买上限', default=999) # 单次购买最大数量
    product_sequence = models.IntegerField(blank=True, null=True) # 排序

    metatag_title_status = models.IntegerField(blank=True, null=True) # ?
    metatag_product_name_status = models.IntegerField(blank=True, null=True) # ?
    metatag_model_status = models.IntegerField(blank=True, null=True) # ?
    metatag_price_status = models.IntegerField(blank=True, null=True) # ?
    metatag_title_tagline_status = models.IntegerField(blank=True, null=True) # ?

    def __unicode__(self):
        return self.product_name

    class Meta:
        db_table = 'product'


class ProductAttribute(models.Model): # 产品属性表
    product = models.ForeignKey(Product) # 产品ID

    class Meta:
        db_table = 'product_attribute'


class ProductDescription(models.Model): # 产品描述表
    product = models.ForeignKey(Product) # 产品ID
    language = models.ForeignKey(Parameter) # 语言ID
    product_name = models.CharField(u'产品名', max_length=64) # 产品名
    product_desc = models.TextField(u'产品描述', blank=True, null=True) # 产品描述
    product_order_desc = models.CharField(u'订购说明', max_length=1000, blank=True, null=True) # 订购说明
    #product_url = models.CharField(max_length=255, blank=True, null=True) # 产品URL
    #product_viewed = models.IntegerField(blank=True, null=True) # ？

    def __unicode__(self):
        return self.product_name

    class Meta:
        db_table = 'product_description'


#class Coupon(models.Model): # 优惠券



class ProductionForAndProductType(models.Model): # 
    pass


#class Product


