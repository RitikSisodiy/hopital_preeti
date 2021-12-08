import threading

from django.contrib import admin
from .models import *
# Register your models here.


# for patient
admin.site.register(patient_record)
admin.site.register(patient_dashB)
#for patient booking checkout
admin.site.register(checkout)

admin.site.register(favourite)

#for patient dashboard

admin.site.register(appoinmentlist)
admin.site.register(billings)
admin.site.register(medical_records)
admin.site.register(prescriptions)
# admin.site.register(favourite)