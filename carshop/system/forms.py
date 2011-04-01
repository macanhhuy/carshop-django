# -*- coding:utf-8

from django import forms

class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'box1'}))
	last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'box1'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'box1'}))
	address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'box1', 'rows':'3', 'cols':'20'}))
	zip = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'box1'}))
	
	country = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown','onchange':'countryChange(this)'}))
	state = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown','onchange':'stateChange(this)'}))
	city = forms.IntegerField(widget=forms.Select(attrs={'class':'dropdown'}))
	
	company = forms.CharField(max_length=100, required=False)
	phone_number = forms.CharField(max_length=32, required=False)
	fax_number = forms.CharField(max_length=32, required=False)
	
	receive_email = forms.CharField(max_length=2)
	
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=128)