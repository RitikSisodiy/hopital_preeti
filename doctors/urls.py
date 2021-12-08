
from django.contrib import admin
from django.urls import path,include
from doctors import views
from doctors.views import schedule

urlpatterns = [

    # path('', views.home, name='home'),
    path('doctor-profile/<int:id>',views.Doctor_profile,name='Doctor_profile'),

    path('doctor-profile/', views.Doctor_profile, name='Doctor_profile'),
    # path('blog-details', views.blog_details, name='blog_details'),
    path('doctor-register', views.Doctor_register, name='Doctor_register'),
    path('login', views.dlogin, name='dlogin'),
    path('logout', views.dlogout, name='dlogout'),
    path('reviews', views.reviews, name='reviews'),
    path('doctor-profile-settings/', views.doctor_profile_setting, name='doctor_profile_setting'),
    path('dislike', views.dislike, name='dislike'),
    path('like', views.like, name='like'),
    path('doctor-dashboard', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointments/', views.appointments, name='appointments'),

    path('appo_delete/', views.appo_delete, name='appo_delete'),

    path('schedule/', views.schedule, name='schedule'),
    path('invoices/', views.invoices, name='invoices'),
    path('chat_doctor/', views.chat_doctor, name='chat_doctor'),
    path('checkup/', views.checkup, name='checkup'),

    path('my_patient/', views.my_patients, name='my_patient'),
    path('allpatient/', views.allpatient, name='allpatient'),
    # path('checkup/', views.checkup, name='checkup'),
    # path('checkup/', views.checkup, name='checkup'),
    # path('checkup/', views.checkup, name='checkup'),
    # path('checkup/', views.checkup, name='checkup'),

    path('chang_pwd/', views.change_password, name='change_password'),
#     path('blog-grid', views.blog_grid, name='blog_grid'),
#     path('blog-list', views.blog_list, name='blog_list'),
#     path('blog-details', views.blog_details, name='blog_details'),
#
]