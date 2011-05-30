# -*- coding: utf-8 -*-

from django.forms import ModelForm
from carshop.order.models import *

class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_street_address')