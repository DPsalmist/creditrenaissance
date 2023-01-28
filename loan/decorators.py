from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Group

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect ('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			else:
				user.groups = 'customers'

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse ('You are not authorised to view this page!')
			
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		print('Group now is ', group)
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customers':
			return redirect('user_page')
		if group == 'chairman':
			return redirect('loan-dashboard')
			#return view_func(request, *args, **kwargs)
		elif group == 'staff' or group == 'chairman':
			return view_func(request, *args, **kwargs)
			
	return wrapper_func
	
