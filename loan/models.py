from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import datetime
# Create your models here.
class Collector(models.Model):
	GENDER = (
		('m', 'Male'),
		('f','Female'),
		('s','Select')
		)
	username = models.ForeignKey(User, null='blank', on_delete=models.CASCADE,related_name='users')
	gender = models.CharField(max_length=20, choices=GENDER, default='select')
	phone = models.CharField(max_length=15, null='blank')
	email = models.EmailField(unique=True, null='blank')

	def __str__(self):
			return self.email

class Group(models.Model):
	title = models.CharField(max_length=20, unique=True, default='Group 1')
	member = models.ForeignKey(Collector, null='blank', on_delete=models.CASCADE,related_name='group_members')

	def __str__(self):
			return self.title

class Loan(models.Model):
	LOAN_STATUS = (
		('Complete', 'Complete'),
		('Incomplete', 'Incomplete'),
		)
	LOAN_REQUEST = (
			('Unapproved','Unapproved'),
			('Pending','Pending'),
			('Approved','Approved')
		)
	title = models.CharField(max_length=30, null='blank')
	slug = models.SlugField(max_length=200, default='title')
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now=True)
	principal = models.IntegerField(null='blank', default=100000)
	balance = models.FloatField(null='blank', default=100000)
	interest_rate = models.FloatField(default=0.1)
	tot_principal = models.CharField(max_length=30, null='blank')
	tot_interest = models.FloatField(max_length=30, null='blank', default=0.0)
	loan_duration = models.IntegerField( default=6)
	payment_status = models.CharField(max_length=30, choices=LOAN_STATUS, default='Incomplete')
	loan_request = models.CharField(max_length=30, choices=LOAN_REQUEST, default='Pending')
	group = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE, default='None',
							 related_name='batches')
	owner = models.ForeignKey(User, null='blank', on_delete=models.CASCADE,related_name='borrowers')
	description = models.TextField()
	frequency = models.IntegerField(null='blank', default=6)

	def __str__(self):
			return '{},{},{},{}, {}, {}'.format(self.owner, self.group, self.loan_request, self.payment_status, 
						self.description, self.tot_interest)

	def get_absolute_url(self):
		return reverse('loan-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-start_date',)
		index_together = (('id', 'slug'),)


