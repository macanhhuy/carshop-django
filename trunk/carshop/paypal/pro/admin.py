#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import split as L
from django.contrib import admin
from paypal.pro.models import PayPalNVP


class PayPalNVPAdmin(admin.ModelAdmin):
	list_display = L("user method flag flag_code iso_create_at")
	
	def iso_create_at(self, obj):
		return obj.created_at.isoformat(' ')
	iso_create_at.short_description = 'create at'

admin.site.register(PayPalNVP, PayPalNVPAdmin)
