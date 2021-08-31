from django.urls import path
from . import views
from.views import (

 #Month1UpdateView,
 Month1DetailView,
 )

app_name = 'months_app'
urlpatterns = [
	path('month1/', views.month1, name='month1'),
    path('month1/<int:pk>/', Month1DetailView.as_view(), name='month1-detail'),
    path('month1-payment-record/', views.month1_update, name='month1_update'),
    path('month2-payment-record/', views.month2_update, name='month2_update'),
    #path('month1/<int:pk>/update', Month1UpdateView.as_view(), name='month1-update'),
]
