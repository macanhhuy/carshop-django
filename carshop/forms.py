# -*- coding:utf-8

from django import forms
from carshop.widgets import NonStyleRadioFieldRenderer
from .models import CountryStateCity

class RegisterForm(forms.Form):
    #def __init__(self, *args, **kwargs):
    #	super(RegisterForm, self).__init__(*args, **kwargs)
    #	self.fields['first_name'].error_messages['required'] = 'fuck you'
    GENDER_CHOICES = ((u'-1', u'Select...'), (u'M', u'Male'), (u'F', u'Female'),)

    RECEIVE_CHOICES = ((u'Y', u'Yes'), (u'N', u'No'))

    COUNTRY_CHOICES = [(u'-1', u'Select...'), ]
    for csc in CountryStateCity.objects.raw('SELECT id, name FROM country_state_city where parent_id is null'):
        COUNTRY_CHOICES.append((csc.id, csc.name))

    STATE_CITY_CHOICES = [(u'-1', u'Select...'), ]

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'box1'}),
                                 error_messages={'required': 'fcuk you!!!'})
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'box1'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'box1'}))
    address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'box1', 'rows': '3', 'cols': '20'}))
    zip = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'box1'}))

    country = forms.IntegerField(
        widget=forms.Select(attrs={'class': 'dropdown', 'onchange': 'countryChange(this)'}, choices=COUNTRY_CHOICES))
    state = forms.IntegerField(
        widget=forms.Select(attrs={'class': 'dropdown', 'onchange': 'stateChange(this)'}, choices=STATE_CITY_CHOICES))
    city = forms.IntegerField(widget=forms.Select(attrs={'class': 'dropdown'}, choices=STATE_CITY_CHOICES))

    gender = forms.CharField(max_length=2, required=False,
                             widget=forms.Select(attrs={'class': 'dropdown'}, choices=GENDER_CHOICES))

    company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'box1'}))
    phone_number = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'class': 'box1'}))
    fax_number = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'class': 'box1'}))

    receive_email = forms.CharField(max_length=2, widget=forms.RadioSelect(renderer=NonStyleRadioFieldRenderer,
                                                                           choices=RECEIVE_CHOICES))

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'box1'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'box1'}))
	
	
