from django.contrib import admin
from .models import Collector, Loan, Group
from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(User)

@admin.register(Collector)
class CollectorAdmin(admin.ModelAdmin):
	list_display = ('username', 'gender','email', 'phone')
	list_filter = ('gender','username', 'email')
	search_fields = ('username', 'email')
	#date_hierarchy = 'loan_status'
	ordering = ('username',)


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
	list_display = ('owner', 'principal','loan_duration', 'loan_request', 'group', 'balance','frequency', 'tot_interest', 
					'payment_status',  'start_date',)
	list_filter = ('owner', 'group','payment_status', 'frequency', 'tot_interest', 'start_date')
	search_fields = ('owner', 'group', 'title','start_date',)
	prepopulated_fields = {'slug': ('title',)}
	#raw_id_fields = ('author',)
	date_hierarchy = 'start_date'
	ordering = ('start_date',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ('title',)
	search_fields = ('title',)
	ordering = ('title',)
