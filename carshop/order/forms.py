# -*- coding:utf-8 -*-

from django.forms.util import ErrorList
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

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=':', empty_permitted=False, instance=None):
        super(self.__class__, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                                             empty_permitted, instance)

        TEMP_CHOICES = [(u'-1', u'Select...'), ]
        if instance.billing_country is not None and instance.billing_country > 0:
            for csc in CountryStateCity.objects.extra(where=['parent_id=%s', ], params=[instance.billing_country, ]):
                TEMP_CHOICES.append((csc.id, csc.name))

            self.fields['billing_state'].widget.choices = TEMP_CHOICES

        TEMP_CHOICES = [(u'-1', u'Select...'), ]
        if instance.billing_state is not None and instance.billing_state > 0:
            for csc in CountryStateCity.objects.extra(where=['parent_id=%s', ], params=[instance.billing_state, ]):
                TEMP_CHOICES.append((csc.id, csc.name))

            self.fields['billing_city'].widget.choices = TEMP_CHOICES

    COUNTRY_CHOICES = [(u'-1', u'Select...'), ]
    for csc in CountryStateCity.objects.raw('SELECT id, name FROM country_state_city where parent_id is null'):
        COUNTRY_CHOICES.append((csc.id, csc.name))

    STATE_CITY_CHOICES = [(u'-1', u'Select...'), ]

    billing_country = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_country', 'class': 'dropdown', 'style': 'width:140px;', 'onchange': 'countryChange(this)'},
                            choices=COUNTRY_CHOICES))

    billing_state = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_state', 'class': 'dropdown', 'style': 'width:120px;', 'onchange': 'stateChange(this)'},
                            choices=STATE_CITY_CHOICES))

    billing_city = forms.IntegerField(
        widget=forms.Select(attrs={'id': 'id_city', 'class': 'dropdown', 'style': 'width:100px;'}, choices=STATE_CITY_CHOICES))

    billing_street_address = forms.CharField(widget=forms.Textarea(attrs={'cols': '30', 'rows': '5'}))

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

