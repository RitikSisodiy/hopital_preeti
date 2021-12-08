
from django.contrib import admin
from django.urls import path,include
from Admin_pharmacy import views

urlpatterns = [

    path('index/', views.index, name='indexs'),
    path('categories/', views.categories, name='categories'),
    path('sales/', views.sales, name='sales'),
    path('transaction/', views.transaction, name='transaction'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('outstock/', views.outstock, name='outstock'),
    path('purchase/', views.purchase, name='purchase'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('order/', views.order, name='order'),
    path('expired/', views.expired, name='expired'),
    path('supplier/', views.suppliers, name='supplier'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('invoice_report/', views.invoice_report, name='invoice_report'),
    path('invoice_views/', views.invoice_views, name='invoice_views'),





    ]