
from django.contrib import admin
from django.urls import path,include
from Admin_hospital import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    ]