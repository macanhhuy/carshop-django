# -*- coding:utf-8 -*-

import datetime

from django.db import models
from django.contrib import admin

class Manufacturer(models.Model):  # 制造商标
    manufacturer_name = models.CharField(u'制造商名', max_length=50) # 制造商名
    date_created = models.DateField() # 创立时间
    time_added = models.DateTimeField(default=datetime.datetime.now()) # 注册时间/添加时间
    time_modified = models.DateTimeField(default=datetime.datetime.now()) # 最后修改时间
    manufacturer_image = models.CharField(max_length=255, blank=True, null=True) # 制造商图片(LOGO)
    manufacturer_desc = models.CharField(max_length=2000, blank=True, null=True) # 描述

    def __unicode__(self):
        return self.manufacturer_name

    class Meta:
        db_table = 'manufacturers'


class CarModel(models.Model):  # 车辆表
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(u'name', max_length=50) # 名字
    time = models.DateTimeField() # -时间
    image = models.CharField(max_length=255, blank=True, null=True) # 制造商图片(LOGO)
    description = models.TextField(blank=True, null=True) # 描述

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'car_models'
		
		

