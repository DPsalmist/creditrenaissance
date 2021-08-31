from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .signals import *

# Create your views here.

def register_page(request):
	form = UserRegisterForm()
	if request.method == 'POST':
		# username = request.POST.get('username')
		# email = request.POST.get('email')
 	# 	password1 = request.POST.get('password1')
 	# 	password2 = request.POST.get('password2')

		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created. You are now able to log in!')
			return redirect ('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

def login_page(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('pwd')
		remember_me = request.POST.get('rmbr')
		user = authenticate(request, username=username, password=password)
		#Check if user exist
		if user is not None:
			login(request, user)
			return redirect ('loan-dashboard')
		else:
			messages.info(request, 'Username or Password incorrect')
	context = {}
	return render(request, 'users/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')
	
@login_required
def profile(request):
	current_user = request.user
	user_role = current_user.groups.all()[0].name

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect ('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
	'u_form':u_form,
	'p_form':p_form,
	'user_role':user_role
	}
	if user_role == 'staff':
		return render(request, 'users/profile.html', context)
	else:
		return render(request, 'users/user_profile.html', context)
