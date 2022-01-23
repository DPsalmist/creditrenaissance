from django.shortcuts import render, redirect
from month.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import ( 
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
# Create your views here.

def month1(request):
	# Get all month1 payments
	month1_payment = Month1.objects.all()

		# Pagination
	page = request.GET.get('page')
	paginator = Paginator(month1_payment, 5)

	try:
		month1_payment = paginator.page(page)
	except PageNotAnInteger:
		month1_payment = paginator.page(1)
	except EmptyPage:
		month1_payment = paginator.page(paginator.num_pages)

	context = {
		'month1_payment':month1_payment,
	}
	return render (request, 'loan/month1.html', context)


class Month1DetailView(DetailView):
	model = Month1
	#template_name = 'month/month1_detail.html'

@login_required
def month1_update(request):
	if request.method == 'POST':
		m1_form = Month1UpdateForm(request.POST, instance=request.user)
		
		if m1_form.is_valid():
			m1_form.save()
			messages.success(request, f'Month1 record has been updated successfully!')
			return redirect ('loan-dashboard')
	else:
		m1_form = Month1UpdateForm(instance=request.user)

	context = {
	'm1_form':m1_form,
	}
	return render(request, 'month/month1_detail.html', context)


@login_required
def month2_update(request):
	if request.method == 'POST':
		m2_form = Month2UpdateForm(request.POST, instance=request.user)
		
		if m2_form.is_valid():
			m2_form.save()
			messages.success(request, f'Month 2 record has been updated successfully!')
			return redirect ('loan-dashboard')
	else:
		m2_form = Month2UpdateForm(instance=request.user)

	context = {
	'm2_form':m2_form,
	}
	return render(request, 'month/month2_update.html', context)
