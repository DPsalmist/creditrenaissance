from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class MyForm(forms.Form):
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bank', 'bvn', 'phone_no', 'address', 'account_no', 'guarantor', 'guarantor_phone_no']

