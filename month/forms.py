from django import forms
from django.contrib.auth.models import User
from .models import *

class Month1UpdateForm(forms.ModelForm):

	class Meta:
		model = Month1
		fields = ['name', 'payment_method', 'loan_month1', 'status',]