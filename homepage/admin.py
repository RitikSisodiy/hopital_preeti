from django.contrib import admin
from .models import *
# Register your models here.



#for subscription
admin.site.register(Newsletter_subscriber)

#for blog details profile
admin.site.register(dr_blogs)