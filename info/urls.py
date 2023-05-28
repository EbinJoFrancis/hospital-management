from django.urls import path
from . import views
# from django.contrib import admin



urlpatterns = [
 
   path('', views.Home,name='home'),
   path('home1/', views.Home1,name='home1'),
   path('contact/', views.Contact,name='contact'),
   path('department/', views.Department,name='department'),
   path('doctor/', views.Doctor,name='doctor'),
   path('appoinment/', views.Appoinment,name='appoinment'),
]
