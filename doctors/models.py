import model_utils
from django.contrib.auth.models import User
from django.db import models
class userType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="userType")
    type = models.CharField(max_length=20,choices=(("1",'patient'),
                ("2","doctor"),("3","pharmacy"),('4','admin'),('5','Pharmacy_admin')))

    def __str__(self):
        return self.user.username
class Dr(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name="Dr")
    name = models.CharField(max_length=30)
    img = models.ImageField()
    qulification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    email=models.EmailField(blank=True)
    fees_starting= models.IntegerField(max_length=5)
    fees_end= models.IntegerField()
    gender = models.CharField(max_length=30)

    def __str__(self):
        return self.name+self.specialization
class Ov_view(models.Model):
    doc = models.OneToOneField(Dr, primary_key=True, related_name='Ov_view', on_delete=models.CASCADE)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.doc.name
class servies_add(models.Model):
    service = models.CharField(max_length=200)

    def __str__(self):
        return self.service
class servi_ses(models.Model):
     dr = models.OneToOneField(Ov_view, on_delete=models.CASCADE, related_name='servi_ses')
     servics=models.ManyToManyField(servies_add,related_name='servies_add')
     def __str__(self):
            return self.dr.doc.name
class specifications_add(models.Model):
    specifications = models.CharField(max_length=200)
    def __str__(self):
        return self.specifications
class Specific_ation(models.Model):
    dr = models.OneToOneField(Ov_view, on_delete=models.CASCADE, related_name='Specification')
    specification=models.ManyToManyField(specifications_add,related_name='Specific_ationss')

    def __str__(self):
        return self.dr.doc.name
class Awards(models.Model):
    dr = models.ForeignKey(Ov_view, on_delete=models.CASCADE, related_name='Awards')
    aw_name = models.CharField(max_length=200)
    aw_year=models.DateField()
    aw_desc = models.TextField(max_length=1000)
    def __str__(self):
        return self.aw_name+self.dr.doc.name
class Educat_ion(models.Model):
    dr = models.ForeignKey(Ov_view, on_delete=models.CASCADE,related_name='Educat_ion')
    univercity = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    YOA = models.DateField()
    YOP = models.DateField()
    def __str__(self):
        return self.univercity+self.dr.doc.name
class Exp_erince(models.Model):
    dr = models.ForeignKey(Ov_view, on_delete=models.CASCADE, related_name='Exp_erince')
    exp_filled = models.CharField(max_length=200)
    YO_exp_start = models.DateField()
    YO_exp_till = models.DateField()
    experince = models.CharField(max_length=100)

    def __str__(self):
        return self.exp_filled+((self.dr.doc.name))
class Buss_Ho(models.Model):
    doc1 = models.OneToOneField(Dr, on_delete=models.CASCADE, primary_key=True, related_name="Buss_Ho")
    dates = models.DateField(auto_now_add=True)
    T1 = models.TimeField()
    T2 = models.TimeField()
    def __str__(self):
        return self.doc1.name
class Hour_S(models.Model):
    dic2 = models.ForeignKey(Buss_Ho, on_delete=models.CASCADE, related_name='Hour_S')
    Time1=models.TimeField()
    Time2=models.TimeField()
    Day=models.CharField(max_length=20)
    def __str__(self):
        return self.Day+(self.dic2.doc1.name)

class reView(models.Model):
    dics = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='reView')
    patient = models.ForeignKey('patient.patient_record',null=True, on_delete=models.CASCADE, related_name='reViewS')
    name = models.CharField(max_length=20)
    review = models.TextField(max_length=1000)
    YES = models.IntegerField()
    NO = models.IntegerField()
    rating = models.IntegerField()
    created=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name + self.dics.name
class Loca_tions(models.Model):
    doc = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name="Loca_tions")
    clinics_name = models.CharField(max_length=100)
    fees = models.IntegerField()
    clinic_add = models.TextField(max_length=300)

    def __str__(self):
        return self.clinics_name+ self.doc.name
class for_bookings(models.Model):
    name= models.ForeignKey(Dr, on_delete=models.CASCADE,blank=True, related_name='for_booking')
    date = models.DateField(blank=True)
    day = models.CharField(max_length=20)

    def __str__(self):
        return self.name.name + (self.day)
class book_timed(models.Model):
      time1= models.TimeField()
      time2 = models.TimeField()

      # def __str__(self):
      #     return self.time1 + self.time2
class book_times(models.Model):
    dr = models.OneToOneField(for_bookings, on_delete=models.CASCADE, related_name='book_times')
    times=models.ManyToManyField(book_timed,related_name='book_timed')


    def __str__(self):
        return self.dr.name.name+self.dr.day
class mypatient(models.Model):
    Dr_names = models.ForeignKey(Dr, on_delete=models.CASCADE, blank=True,
                                 related_name='mypatients')
    pa_names=models.ForeignKey('patient.patient_record',null=True, on_delete=models.CASCADE,blank=True, related_name='mypatient')
    # def __str__(self):
    #     return  self.pa_names.name

