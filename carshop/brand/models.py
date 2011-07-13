# -*- coding:utf-8 -*-

import datetime

from django.db import models
from django.contrib import admin

class Brand(models.Model):  # 车品牌
    name = models.CharField(u'品牌名', max_length=50) # 品牌名
    url_name = models.CharField(u'url名', max_length=50)
    time_added = models.DateTimeField(default=datetime.datetime.now()) # 注册时间/添加时间
    time_modified = models.DateTimeField(default=datetime.datetime.now()) # 最后修改时间
    image = models.CharField(max_length=255, blank=True, null=True) # 制造商图片(LOGO)
    desc = models.CharField(max_length=2000, blank=True, null=True) # 描述

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'brands'

class BrandSeries(models.Model): # 系列
    
    brand = models.ForeignKey(Brand)
    
    name = models.CharField(u'系列', max_length=100)
    date_created = models.DateField(default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        db_table = 'brand_series'

class Car(models.Model):  # 车辆表
    brand_series = models.ForeignKey(BrandSeries)
    
    name = models.CharField(u'name', max_length=50) # 名字
    time = models.DateTimeField() # -时间
    description = models.TextField(blank=True, null=True) # 描述

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'cars'
		
		

