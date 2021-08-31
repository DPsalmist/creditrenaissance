from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Loan
from month.models import *


class LoanForm(ModelForm):
	class Meta:
		model = Loan
		fields = '__all__'
		exclude = ['user']


class Month1UpdateForm(forms.ModelForm):
	class Meta:
		model = Month1
		fields = ['name', 'payment_method', 'loan_month1', 'status',]

class Month2UpdateForm(forms.ModelForm):
	class Meta:
		model = Month2
		fields = ['name', 'payment_method', 'loan_month2', 'status',]

class Month3UpdateForm(forms.ModelForm):
	class Meta:
		model = Month3
		fields = ['name', 'payment_method', 'loan_month3', 'status',]

class Month4UpdateForm(forms.ModelForm):
	class Meta:
		model = Month4
		fields = ['name', 'payment_method', 'loan_month4', 'status',]

class Month5UpdateForm(forms.ModelForm):
	class Meta:
		model = Month5
		fields = ['name', 'payment_method', 'loan_month5', 'status',]

class Month6UpdateForm(forms.ModelForm):
	class Meta:
		model = Month6
		fields = ['name', 'payment_method', 'loan_month6', 'status',]

class Month7UpdateForm(forms.ModelForm):
	class Meta:
		model = Month7
		fields = ['name', 'payment_method', 'loan_month7', 'status',]