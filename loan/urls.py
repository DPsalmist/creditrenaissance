from django.urls import path
from . import views
from.views import (
 LoanListView, 
 LoanDetailView,
 LoanCreateView,
 LoanUpdateView,
 LoanDeleteView,
 UserLoanListView,
 SearchListView,

 Month1DetailView,
 Month1CreateView,
 Month2CreateView,
 Month3CreateView,
 Month4CreateView,
 Month5CreateView,
 Month6CreateView,
 Month7CreateView,
 )

#app_name = 'loan_app'

urlpatterns = [
    # Index
	path('', views.index, name='loan-index'),
	path('user/', views.user_page, name='user_page'),
	path('blog/', views.blog, name='loan-blog'),

    # Dashboard 
	path('dashboard/', views.dashboard, name='loan-dashboard'),
	path('user_search/', SearchListView.as_view(), name='search-index'),

    # Loans
	#path('', LoanListView.as_view(), name='loan-index'),
	path('user/<str:username>', UserLoanListView.as_view(), name='user-loans'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('loan/<int:pk>/update', LoanUpdateView.as_view(), name='loan-update'),
    path('loan/<int:pk>/delete', LoanDeleteView.as_view(), name='loan-delete'),
    path('loan/new/', LoanCreateView.as_view(), name='loan-create'),

    # Monthly Payments
    path('month1/', views.month1, name='month1'),
    path('all-loan-payments/', views.all_loan_payments, name='all_loan_payments'),
    path('month1/<int:pk>/', Month1DetailView.as_view(), name='month1-detail'),
    path('month1-payment-records/', Month1CreateView.as_view(), name='month1-update'),
    path('month2-payment-record/', Month2CreateView.as_view(), name='month2-update'),
    path('month3-payment-record/', Month3CreateView.as_view(), name='month3-update'),
    path('month4-payment-record/', Month4CreateView.as_view(), name='month4-update'),
    path('month5-payment-record/', Month5CreateView.as_view(), name='month5-update'),
    path('month6-payment-record/', Month6CreateView.as_view(), name='month6-update'),
    path('month7-payment-record/', Month7CreateView.as_view(), name='month7-update'),
]
