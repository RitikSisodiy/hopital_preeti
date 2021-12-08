
from django.contrib import admin
from django.urls import path,include
from pharmacy import views

urlpatterns = [

    # path('', views.home, name='home'),
    path('pharmacy-search', views.pharmacy_search, name='pharmacy_search'),
    path('pharmacy-details', views.pharmacy_details, name='pharmacy_details'),
    path('product-all', views.product_all, name='product_all'),
    path('product-description', views.product_description, name='product_description'),
    path('cart', views.medicine_cart, name='medicine_cart'),
    path('addcart', views.add_to_cart, name='add_to_cart'),
    path('pharmacy-register/', views.pharmacy_register, name='pharmacy_register'),
    path('minus',views.minus,name='minus'),
    path('plus', views.plus, name='plus'),
    path('delete', views.delete, name='delete'),
    path('product_checkout',views.product_checkout,name='product_checkout'),
    path('product-order', views.product_order, name='product_order'),
    path('payment-success', views.payment_success, name='payment_success'),

]