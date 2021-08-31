from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Month1)
class Month1Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month1', 'loan_group1', 'status')
	search_fields = ('loan_month1',)
	list_filter = ('name','loan_group1','loan_month1', 'status')

@admin.register(Month2)
class Month2Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month2','loan_group2', 'status')
	search_fields = ('loan_month2',)
	list_filter = ('name','loan_group2','loan_month2')

@admin.register(Month3)
class Month3Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month3', 'loan_group3', 'status')
	search_fields = ('loan_month3',)
	list_filter = ('name','loan_group3','loan_month3')

@admin.register(Month4)
class Month4Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month4', 'loan_group4', 'status')
	search_fields = ('loan_month4',)
	list_filter = ('name','loan_group4','loan_month4')

@admin.register(Month5)
class Month5Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month5', 'loan_group5', 'status')
	search_fields = ('loan_month5',)
	list_filter = ('name','loan_group5','loan_month5')

@admin.register(Month6)
class Month6Admin(admin.ModelAdmin):
	list_display = ('name', 'loan_month6', 'loan_group6', 'status')
	search_fields = ('loan_month6',)
	list_filter = ('name','loan_group6','loan_month6')