from django.db import models
import model_utils
from django.contrib.auth.models import User
# Create your models here.
from doctors.models import Dr


class patient_record(models.Model):
        patient = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name="patient_record")
        name = models.CharField(max_length=50)
        img = models.ImageField()
        mobile = models.IntegerField()
        city = models.CharField(max_length=50)
        address = models.TextField()
        email = models.EmailField()
        DOB= models.DateField()
        gender = models.CharField(max_length=50)
        Blood_group = models.CharField(max_length=20)
        age = models.IntegerField()

        def __str__(self):
            return self.name
class patient_dashB(models.Model):
    patient_name = models.OneToOneField(patient_record, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_dashB")
    heart_rate = models.IntegerField()
    BP_mg = models.IntegerField()
    BP_dl = models.IntegerField()
    body_temp= models.IntegerField()
    Glucose_Level_up = models.IntegerField()
    Glucose_Level_to = models.IntegerField()
    BMI_Status = models.IntegerField()
    Heart_Rate_Status= models.IntegerField()
    FBC_Status = models.IntegerField()
    Weight_Status= models.IntegerField()

    def __str__(self):
        return self.patient_name.name
class checkout(models.Model):
    dr_name=models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='checkout')
    patient=models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='checkouts')
    email=models.EmailField()
    phone=models.IntegerField()
    date=models.DateField()
    time1=models.TimeField()
    time2=models.TimeField()
    card_name=models.CharField(max_length=20)
    card_no=models.IntegerField()
    cvv=models.IntegerField()
    exp_year=models.IntegerField()
    exp_month=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.dr_name.name+(self.patient.name)
class appoinmentlist(models.Model):
    doctor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='appoinmentlist')
    patient = models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='appoinmentlists')
    date = models.DateField()
    time1 = models.TimeField()
    time2 = models.TimeField()
    card_name = models.CharField(max_length=20)
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    exp_year = models.IntegerField()
    exp_month = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.doctor.name + (self.patient.name)

class favourite(models.Model):
    dr_name=models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='favourite')
    pa_name=models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='favs')

    def __str__(self):
        return self.dr_name.name + (self.pa_name.name)
class prescriptions(models.Model):
    patient = models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='prescription')
    date = models.DateField()
    doctor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='prescription')

    def __str__(self):
        return self.patient.name+self.doctor.name
class medical_records(models.Model):
    patient = models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='medical_record')
    desc=models.CharField(max_length=20)
    attachment = models.FileField()
    date = models.DateField()
    doctor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='medical')

    def __str__(self):
        return self.patient.name+self.doctor.name
class billings(models.Model):
    patient = models.ForeignKey(patient_record, on_delete=models.CASCADE, related_name='billingss')
    doctor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='bill')
    invoice_no = models.IntegerField()
    paid_on_date = models.DateField()
    amount = models.IntegerField()
#
    def __str__(self):
        return self.patient.name+self.doctor.name