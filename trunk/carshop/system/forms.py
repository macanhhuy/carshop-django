# -*- coding:utf-8

from django import forms
from carshop.system.widgets import NonStyleRadioFieldRenderer


class RegisterForm(forms.Form):
	
	RECEIVE_CHOICES = ((u'Y', u'Yes'), (u'N', u'No'))

	first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'box1'}))
	last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'box1'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'box1'}))
	address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'box1', 'rows':'3', 'cols':'20'}))
	zip = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'box1'}))
	
	country = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown','onchange':'countryChange(this)'}))
	state = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown','onchange':'stateChange(this)'}))
	city = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown'}))
	
	company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'box1'}))
	phone_number = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'class':'box1'}))
	fax_number = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'class':'box1'}))
	
	receive_email = forms.CharField(max_length=2, widget=forms.RadioSelect(renderer=NonStyleRadioFieldRenderer, choices=RECEIVE_CHOICES))
	
	username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'box1'}))
	password = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'box1'}))
	
	
