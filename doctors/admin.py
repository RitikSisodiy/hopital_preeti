import threading

from django.contrib import admin
from .models import *
# # Register your models here.
admin.site.register(Dr)
#for doctor profile overview
admin.site.register(Ov_view)
admin.site.register(Specific_ation)
admin.site.register(specifications_add)
admin.site.register(Educat_ion)
admin.site.register(Awards)
admin.site.register(servi_ses)
admin.site.register(servies_add)
admin.site.register(Exp_erince)

#for doctor profile review
admin.site.register(reView)

#for doctor profile location
admin.site.register(Loca_tions)

#for doctor profile bussness hour
admin.site.register(Buss_Ho)
admin.site.register(Hour_S)



# for patient
admin.site.register(userType)

#for booking appointment
admin.site.register(for_bookings)

admin.site.register(book_times)
admin.site.register(book_timed)


admin.site.register(mypatient)