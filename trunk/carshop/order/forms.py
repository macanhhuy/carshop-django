# -*- coding: utf-8 -*-
#from django.forms.util import ErrorList
from django.forms import ModelForm
from carshop.order.models import *

class OrderForm(ModelForm):
    
#    def __init__(self, request, data=None, files=None, auto_id='id_%s', prefix=None,
#                 initial=None, error_class=ErrorList, label_suffix=':',
#                 empty_permitted=False, instance=None):
#        super(self.__class__, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)
        
#        self.customer = request.user
	

    
    class Meta:
        model = Order

        fields = ('customer_name', 'customer_company', 'customer_street_address', 'customer_suburb', 'customer_city', 'customer_postcode', 'customer_state', 'customer_country', 'customer_telephone', 'customer_email_address')

