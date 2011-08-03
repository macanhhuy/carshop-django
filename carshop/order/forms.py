# -*- coding:utf-8 -*-
#from django.forms.util import ErrorList
from django.forms import ModelForm
from django import forms
from ..models import CountryStateCity
from .models import *

class OrderForm(ModelForm):

#    def __init__(self, request, data=None, files=None, auto_id='id_%s', prefix=None,
#                 initial=None, error_class=ErrorList, label_suffix=':',
#                 empty_permitted=False, instance=None):
#        super(self.__class__, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance)

#        self.customer = request.user
    COUNTRY_CHOICES = [(u'-1', u'Select...'), ]
    for csc in CountryStateCity.objects.raw('SELECT id, name FROM country_state_city where parent_id is null'):
        COUNTRY_CHOICES.append((csc.id, csc.name))
    STATE_CHOICES = [(u'-1', u'Select...'), ]

    CITY_CHOICES = [(u'-1', u'Select...'), ]

    billing_country = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_country', 'class': 'dropdown', 'onchange': 'countryChange(this)'},
                            choices=COUNTRY_CHOICES))

    for csc in CountryStateCity.objects.extra(where=['parent_id=%s', ], params=[billing_country, ]):
        STATE_CHOICES.append((csc.id, csc.name))
    billing_state = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_state', 'class': 'dropdown', 'onchange': 'stateChange(this)'},
                            choices=STATE_CHOICES))

    for csc in CountryStateCity.objects.extra(where=['parent_id=%s', ], params=[billing_state, ]):
        CITY_CHOICES.append((csc.id, csc.name))
    billing_city = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_city', 'class': 'dropdown'}, choices=CITY_CHOICES))

    class Meta:
        model = Order

        fields = (
        'billing_country',
        'billing_state',
        'billing_city',
        'billing_first_name',
        'billing_last_name',
        'billing_company',
        'billing_street_address',
        'billing_suburb',
        'billing_postcode',)

