from django.contrib import admin
from django.urls import path, include
from patient import views

urlpatterns = [

    # path('', views.home, name='home'),
    path('chang_pwd/', views.change_password, name='change_password'),
    path('booking', views.booking, name='booking'),
    path('checkout/', views.checkouts, name='checkout'),
    # path('blog-details', views.blog_details, name='blog_details'),
    # path('login', views.dlogin, name='dlogin'),
    # path('logout', views.dlogout, name='dlogout'),
    path('booking-success', views.booking_success, name='booking_success'),
    path('patient-register', views.patient_register, name='patient_register'),
    path('profile-settings', views.profile_setting, name='profile_setting'),
    path('order_list', views.order_list, name='order_list'),
    path('add_medical_record', views.add_medical_record, name='add_medical_record'),
    path('patient-profile', views.patient_profile, name='patient_profile'),
    path('invoice_view/', views.invoice_view, name='invoice_view'),
    path('favourites', views.favourites, name='favourites'),
    path('favt', views.favt, name='favt'),
    path('search/', views.Search, name='search'),
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),

    # path('blog-grid', views.blog_grid, name='blog_grid'),
    # path('blog-list', views.blog_list, name='blog_list'),
    # path('blog-details', views.blog_details, name='blog_details'),

]