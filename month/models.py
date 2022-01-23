from django.db import models
from loan.models import Loan, Group
from django.utils import timezone

# Create your models here.
class Month1(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 1')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group1 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month1 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	paid_date = models.DateTimeField(null='blank')
	status = models.BooleanField(default=False)

	def __str__(self):
		return '{}'.format(self.status)

class Month2(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 2')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group2 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month2 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Month3(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 3')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group3 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month3 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Month4(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 4')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group4 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month4 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Month5(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 5')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group5 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month5 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Month6(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 6')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group6 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month6 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Month7(models.Model):
	name = models.CharField(max_length=30, null='blank', default='month 7')
	methods = (
		('Cash', 'Cash'),
		('Transfer', 'Transfer'),
		('Other', 'Other')
		)
	payment_method = models.CharField(max_length=30, choices=methods, default='Cash')
	loan_group7 = models.ForeignKey(Group, null='blank', on_delete=models.CASCADE)
	loan_month7 = models.OneToOneField(Loan, null='blank', on_delete=models.CASCADE, unique=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name