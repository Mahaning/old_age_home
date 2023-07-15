# dj_razorpay/urls.py

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
	path('', views.homepage, name='/'),
	path('payment/', views.payment, name='payment'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('story/', views.story, name='story'),
    
	path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
	path('admin/', admin.site.urls),
]
