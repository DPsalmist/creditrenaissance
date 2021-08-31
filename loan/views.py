from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Loan, Collector, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from users.models import Profile
from month.models import *
from month.urls import app_name
import datetime
from django.db.models import Q
from django.views.generic import ( 
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)

# INDEX VIEWS
def index(request):
	return render (request, 'loan/index.html')
# Blog View 
def blog(request):
	return render (request, 'loan/blog.html')

# STAFF DASHBOARD VIEW
@login_required(login_url='login')
@admin_only
def dashboard(request):
	# Get Loan group
	group = request.GET.get('group')
	# Get Freuency
	frequency = request.GET.get('frequency')
	# Get User
	user = request.user
	#print('Current user from staff dashboard:', user)
	user_role = user.groups.all()[0].name
	#print('Current user role from staff dashboard:', user_role)

	# Get all months/weeks
	month1_payment = Month1.objects.all()

	# Get Loans
	loan = Loan.objects.all()
	# Get Total Loans
	tot_loans = loan.filter(loan_request='Approved').count()
	# Pending loan requests
	pending_loans = loan.filter(loan_request='Pending').count()
	all_pending_loans = loan.filter(loan_request='Pending')
	print('These are all_pending_loans:', all_pending_loans)

	# Get user pic
	user_profile = Profile.objects.filter(user=user)
	for user_profile in user_profile:
		user_img = user_profile.image
	user_img = user_img

	# Calculate cummulative interest
	cumm_tot_interest = 0
	
	for i in loan:
		cumm_tot_interest += i.tot_interest
		#print(' Tot interest =', int(i.tot_interest), 'Cummulative tot_interest = ', int(cumm_tot_interest))
		#print('The cummulative interest is #', cumm_tot_interest)

	# Format the cumm_tot_interest to 2 dp.
	cumm_tot_interest = '%1.2f' %(cumm_tot_interest)

	# Group Filter 
	if group == None:
		loans = Loan.objects.all()
	else:
		loans = Loan.objects.filter(group__title= group)

	# Frequency Filter
	freqs =  [0,1,2,3,4,5,6]
	if frequency == None:
		loans = Loan.objects.all()
	else:
		loans = Loan.objects.filter(frequency=frequency)

	# Pagination
	page = request.GET.get('page')
	paginator = Paginator(loans, 4)
	try:
		loans = paginator.page(page)
	except PageNotAnInteger:
		loans = paginator.page(1) #If page is not an integer deliver the first page
	except EmptyPage:
		loans = paginator.page(paginator.num_pages)

	context = {
		'page':page,
		'loans':loans,
		'month1_payment':month1_payment,
		'user_role':user_role,
		'loans_pic': Loan.objects.all(),
		'user':user,
		'user_img':user_img,
		'tot_loans':tot_loans,
		'pending_loans':pending_loans,
		'all_pending_loans':all_pending_loans,
		'cumm_tot_interest': cumm_tot_interest,
		'groups':Group.objects.all(),
		'freqs': freqs
	}
	return render (request, 'loan/dashboard.html', context)


# USER DASHBOARD VIEW
@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def user_page(request):
	# Get loan user
	current_user = request.user
	#print('Current User from user_page:', current_user)
	user_role = current_user.groups.all()[0].name
	#print('Current user role from user_page:', user_role)
	loan_owner = Loan.objects.filter(owner=current_user)

	# Pending loan requests
	pending_loans = loan_owner.filter(loan_request='Pending').count() 

	# Get user's loan start_date
	#loan_start_date = Loan.objects.filter(owner=current_user)
	loan_start_date = loan_owner.order_by('start_date')
	print('Loan start date:', loan_start_date)

	# Get user's total loans
	my_loans = Loan.objects.filter(owner=current_user).order_by('-start_date')
	my_total_loans = Loan.objects.filter(owner=current_user).count()

	# Pagination
	page = request.GET.get('page')
	paginator = Paginator(my_loans, 3)

	try:
		my_loans = paginator.page(page)
	except PageNotAnInteger:
		my_loans = paginator.page(1) 
	except EmptyPage:
		my_loans = paginator.page(paginator.num_pages)

	context = {
		'page':page,
		'loan_start_date':loan_start_date,
		'pending_loans':pending_loans,
		'user_role':user_role,
		'current_user':current_user, 		
		'my_total_loans':my_total_loans,
		'my_loans':my_loans,
		}
	return render (request, 'loan/user_dashboard.html', context)


# MONTHLY PAYMENT VIEWS
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

def all_loan_payments(request):
	return render (request, 'loan/all_loan_payments.html',)

class Month1DetailView(DetailView):
	model = Month1
	#template_name = 'month/month1_detail.html'

class Month1CreateView(LoginRequiredMixin, CreateView):
	model = Month1
	fields = ['name', 'payment_method', 'loan_month1', 'status',]
	success_url = '/dashboard/'

class Month2CreateView(LoginRequiredMixin, CreateView):
	model = Month2
	fields = ['name', 'payment_method', 'loan_month2', 'status',]
	success_url = '/dashboard/'

class Month3CreateView(LoginRequiredMixin, CreateView):
	model = Month3
	fields = ['name', 'payment_method', 'loan_month3', 'status',]
	success_url = '/dashboard/'

class Month4CreateView(LoginRequiredMixin, CreateView):
	model = Month4
	fields = ['name', 'payment_method', 'loan_month4', 'status',]
	success_url = '/dashboard/'

class Month5CreateView(LoginRequiredMixin, CreateView):
	model = Month5
	fields = ['name', 'payment_method', 'loan_month5', 'status',]
	success_url = '/dashboard/'

class Month6CreateView(LoginRequiredMixin, CreateView):
	model = Month6
	fields = ['name', 'payment_method', 'loan_month6', 'status',]
	success_url = '/dashboard/'

class Month7CreateView(LoginRequiredMixin, CreateView):
	model = Month7
	fields = ['name', 'payment_method', 'loan_month7', 'status',]
	success_url = '/dashboard/'

# LOAN VIEWS 
class UserLoanListView(ListView):
	model = Loan
	template_name = 'loan/user_loans.html' 
	context_object_name = 'my_loans'
	ordering = ['-start_date'] 
	paginate_by = 5

	def get_queryset(self):
		#getting the username from the url 
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Loan.objects.filter(owner=user).order_by('-start_date')


class SearchListView(ListView):
    model = Loan
    context_object_name = 'search_results'
    template_name = 'loan/user_search.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	query = self.request.GET.get('q', '')
    	searched_user = User.objects.filter(username__contains=query).first()
    	user = get_object_or_404(User, username=searched_user)
    	#print ('user get_object_or_404 returns: ',user, 'and', user.id)
    	context['search_results'] = Loan.objects.filter(owner=user.id).order_by('-start_date')
    	context['user'] = user
    	return context

class LoanListView(ListView):
	model = Loan
	template_name = 'loan/index.html'
	context_object_name = 'loans'
	ordering = ['-start_date']
	paginate_by = 5

class LoanDetailView(DetailView):
	model = Loan
	
	# To get the current usr role
	def get_object(self):
		current_user = self.request.user
		print('Current User from Loan DetailView:', current_user)
		user_role = current_user.groups.all()[0].name
		print('Current user role from Loan DetailView:', user_role)
		return current_user
	
	# To get individual object of the loan
	def get_object(self):
		obj = super().get_object()
		# Storing initial loan records
		loan_id = obj.id
		month1 = Month1.objects.all()
		# Getting user's paid month 
		month1_loan_status = Month1.objects.filter(loan_month1__id__exact=loan_id).filter(status__exact=True).last()
		month2_loan_status = Month2.objects.filter(loan_month2__id__exact=loan_id).filter(status__exact=True).last()
		month3_loan_status = Month3.objects.filter(loan_month3__id__exact=loan_id).filter(status__exact=True).last()
		month4_loan_status = Month4.objects.filter(loan_month4__id__exact=loan_id).filter(status__exact=True).last()
		month5_loan_status = Month5.objects.filter(loan_month5__id__exact=loan_id).filter(status__exact=True).last()
		month6_loan_status = Month6.objects.filter(loan_month6__id__exact=loan_id).filter(status__exact=True).last()
		
		#print('Loan ID is ',loan_id)
		#print('Month 1 contains ', month1)
		print('Starting....this loan\'s month 1 status is ',month1_loan_status)
		principal = obj.principal
		interest_rate = obj.interest_rate
		duration = obj.loan_duration
		balance = obj.balance
		tot_interest = obj.tot_interest
		freq = obj.frequency
		# Loan Repayment Calculation
		# Testing
		print('###################################')
		print('The principal is',principal)
		#print('The interest is',interest)
		print('')
		#print('The monthly principal is #',mont_prin)
		print('The total interest is #',tot_interest)
		print('###################################')
		#Loop through loan's duration
		if month1_loan_status:
			print('MONTH PAID')
		else:
			print('MONTH NOT PAID')

		if month1_loan_status:
			print('Loan Status: Incomplete')
			for i in range(1, int(duration)+1):
				interest = (principal * interest_rate)
				mont_prin = (principal / duration)
				fixed_mont_prin = (principal / duration)
				if i == 1 and month1_loan_status and freq == 6:
					#update tot_interest, tot_mont_prin and freq.
					tot_interest = interest
					tot_mont1_repay = interest + mont_prin
					freq1 = freq - 1

					obj.balance = principal - mont_prin
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont1_repay
					obj.frequency = freq1
					obj.save()
				elif i == 2 and month2_loan_status and freq == 5:
					mont_prin = (principal / duration)
					new_prin2 = balance - mont_prin
					interest2 = (balance * interest_rate)
					tot_mont2_repay = interest2 + mont_prin
					tot_interest = tot_interest + interest2
					freq2 = freq - 1
					
					obj.balance = new_prin2
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont2_repay
					obj.frequency = freq2
					obj.save()
				elif i == 3 and month3_loan_status and freq == 4:
					mont_prin = (principal / duration)
					new_prin3 = balance - mont_prin
					interest3 = (balance * interest_rate)
					tot_mont3_repay = interest3 + mont_prin
					tot_interest = tot_interest + interest3
					freq3 = freq - 1

					obj.balance = new_prin3
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont3_repay
					obj.frequency = freq3
					obj.save()
				elif i == 4 and month4_loan_status and freq == 3:
					mont_prin = (principal / duration)
					new_prin4 = balance - mont_prin
					interest4 = (balance * interest_rate)
					tot_mont4_repay = interest4 + mont_prin
					tot_interest = tot_interest + interest4
					freq4 = freq - 1

					obj.balance = new_prin4
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont4_repay
					obj.frequency = freq4
					obj.save()
				elif i == 5 and month5_loan_status and freq == 2:
					mont_prin = (principal / duration)
					new_prin5 = balance - mont_prin
					interest5 = (balance * interest_rate)
					tot_mont5_repay = interest5 + mont_prin
					tot_interest = tot_interest + interest5
					freq5 = freq - 1

					obj.balance = new_prin5
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont5_repay
					obj.frequency = freq5
					obj.save()
				elif i == 6 and month6_loan_status and freq == 1:
					mont_prin = (principal / duration)
					new_prin6 = balance - mont_prin
					interest6 = (balance * interest_rate)
					tot_mont6_repay = interest6 + mont_prin
					tot_interest = tot_interest + interest6
					freq6 = freq - 1

					obj.balance = new_prin6
					obj.tot_interest = tot_interest
					obj.tot_mont_repay = tot_mont6_repay
					obj.frequency = freq6
					obj.save()
					# print('Thanks')
				elif freq == 0:
					#update loan's status
					old_stat = obj.payment_status
					loan_stat =  'complete'
					obj.payment_status = loan_stat
					print('Lets see: ',old_stat)
					print('Lets see: ',obj.payment_status)
					#loan_stat = Loan.objects.filter()[7]
					obj.save()
					# print('Loan Payment Status: COMPLETE!')
					# print()
					# print('Interest is: ', tot_interest)
					# print('Total Interest is now: ', tot_interest)
					# print('###################################')

		else:
			print('Goodbye...')

		return obj

class LoanCreateView(LoginRequiredMixin, CreateView):
	model = Loan
	fields = ['title', 'principal', 'group','description']

	#overriding the form valid method
	def form_valid(self, form):
		form.instance.owner  = self.request.user
		return super().form_valid(form)

class LoanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Loan
	fields = ['title', 'principal', 'description']
	
	def form_valid(self, form):
		form.instance.owner  = self.request.user
		return super().form_valid(form)

	#test function to make only an authorised user update a post
	def test_func(self):
		loan = self.get_object()
		if self.request.user == loan.owner:
			return True
		return False

class LoanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Loan
	success_url = '/dashboard/'

	#test function to make only an authorised user delete a post
	def test_func(self):
		loan = self.get_object()
		if self.request.user == loan.owner:
			return True
		return False

