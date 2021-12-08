import threading

from django.contrib import admin
from .models import *
# # Register your models here.
#for pharmacy profile
admin.site.register(pharmacy)
admin.site.register(pha_Oview)
admin.site.register(pha_awards)
admin.site.register(pha_buss)
admin.site.register(pha_loc)
admin.site.register(pha_review)

# for pharmacy products
admin.site.register(pha_product)
admin.site.register(pha_apply)
admin.site.register(pha_highlight)

# for cart product order
admin.site.register(pharmacy_prod_order)

#for pharmacy new register user
# admin.site.register(pharmacy_register_record)
#for add to pharmacy cart
admin.site.register(product_cart)
