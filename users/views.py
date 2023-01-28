from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
#from loan.models import Group
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .signals import *

# Create your views here.

def register_page(request):
	form = UserRegisterForm()
	if request.method == 'POST':
		print('Post request received!')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('pwd1')
		password2 = request.POST.get('pwd2')
		group = 'customers'

		if password1 != password2:
			messages.error(request, f"Your passwords don't match! Please make sure they are the same.")
		if User.objects.filter(email=email).exists():
			messages.error('Email already in use!')
		if User.objects.filter(username=username).exists():
			messages.error('Username already in use! Please try a different username.')
		else:
			user = User.objects.create_user(username, email)
			group = Group.objects.get(name='customers')
			user.groups.add(group) 
			user.set_password(password1)
			user.save()
			messages.success(request, f'Your account has been created. You are now able to log in!')
			print(f'{username} created successfully!!! with group {group}')

			return redirect ('login')


		# form = UserRegisterForm(request.POST)
		# if form.is_valid():
		# 	form.save()
		# 	print('Form is valid!')
		# 	username = form.cleaned_data.get('username')
		# 	password = request.POST.get('pwd1')
		# 	user = authenticate(username=username, password=password)
		# 	login(request, user)
		# 	messages.success(request, f'Your account has been created. You are now able to log in!')
		# 	return redirect ('login')
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
			print('Authentication successful!')
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
