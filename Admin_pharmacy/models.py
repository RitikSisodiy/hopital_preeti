from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from pharmacy.models import pha_product,pharmacy

class pharmacy_admin_record(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='pharmacy_admin_record')
    name=models.CharField(max_length=30)
    email = models.EmailField()
    img=models.ImageField()
    dob = models.DateField(blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    zipcode = models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    state = models.CharField(max_length=30,blank=True,null=True)
    country = models.CharField(max_length=30,blank=True,null=True)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class supplier(models.Model):
    user=models.ForeignKey(pharmacy,on_delete=models.CASCADE,blank=True,null=True,related_name='suppliers')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    img = models.ImageField()
    product = models.ForeignKey(pha_product,on_delete=models.CASCADE,blank=True,null=True,related_name='supplier')
    mobile = models.IntegerField()
    company = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return self.name
class category(models.Model):
    cate = models.CharField(max_length=30)
    date_created=models.DateField(auto_now=True)
    def __str__(self):
        return self.cate


class Purchase(models.Model):
    pharmacys = models.ForeignKey(pharmacy, on_delete=models.CASCADE, blank=True, null=True, related_name='pharmacy')
    med_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    supplir = models.ForeignKey(supplier,on_delete=models.CASCADE,blank=True,null=True,related_name='purchase')
    quntity = models.IntegerField()
    ex_date = models.CharField(max_length=30)
    created_date=models.DateField(auto_now=True)
    img = models.ImageField()

    def __str__(self):
        return self.med_name

class setting(models.Model):
    pharmacy=models.OneToOneField(pharmacy,on_delete=models.CASCADE,related_name='setting')
    webname=models.CharField(max_length=30)
    weblogo=models.ImageField()
    favican=models.ImageField()

    def __str__(self):
        return self.webname






