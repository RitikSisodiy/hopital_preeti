from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'admin_hospital/index.html')

def appointment_list(request):
    return render(request,'admin_hospital/appointment-list.html')

def specialities(request):
    return render(request,'admin_hospital/specialities.html')

def doctor_list(request):
    return render(request,'admin_hospital/doctor-list.html')

def patient_list(request):
    return render(request,'admin_hospital/patient-list.html')

def reviews(request):
    return render(request,'admin_hospital/reviews.html')

def transactions_list(request):
    return render(request,'admin_hospital/transactions-list.html')

def settings(request):
    return render(request,'admin_hospital/settings.html')

# def dashboard(request):
#     return render(request,'admin_hospital/index.html')
