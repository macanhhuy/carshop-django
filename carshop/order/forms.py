# -*- coding: utf-8 -*-

from django.forms import ModelForm
from carshop.order.models import *

class OrderForm(ModelForm):
    

    
    def __init__(self, request):
        super(self.__class__, self).__init__()
        self.customer = request.user
	
    class Meta:
        model = Order

        fields = ('customer_name', 'customer_street_address')

