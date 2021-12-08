from django.db import models
from django.contrib.auth.models import User
from doctors.models import userType
# Create your models here.

# class pharmacy_register_record(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pharmacy_register_record")
#     name=models.CharField(max_length=40)
#     email=models.EmailField()
#
#     def __str__(self):
#         return self.name

class pharmacy(models.Model):
    # user = models.OneToOneField(userType, on_delete=models.CASCADE,default='ppp',blank=True, null=True, related_name="pharmacy_register_record")
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True,related_name='pharmacy')
    img=models.ImageField()
    name=models.CharField(max_length=200)
    email = models.EmailField(null=True)
    address=models.TextField(max_length=1000)
    degree=models.CharField(max_length=500)
    contact=models.IntegerField()
    opentime=models.TimeField()
    clostime=models.TimeField()
    def __str__(self):
        return self.name
class pha_Oview(models.Model):
    doc = models.OneToOneField(pharmacy, primary_key=True, related_name='pha_Oview', on_delete=models.CASCADE)
    about = models.TextField(max_length=500)
    def __str__(self):
        return self.doc.name
class pha_awards(models.Model):
    dr = models.ForeignKey(pha_Oview, on_delete=models.CASCADE, related_name='pha_awards')
    aw_name = models.CharField(max_length=200)
    aw_year=models.DateField()
    aw_desc = models.TextField(max_length=1000)
    def __str__(self):
        return self.aw_name+self.dr.doc.name
class pha_review(models.Model):
    dics = models.ForeignKey(pharmacy, on_delete=models.CASCADE, related_name='pha_review')
    name = models.CharField(max_length=20)
    review = models.TextField(max_length=1000)
    YES = models.IntegerField()
    NO = models.IntegerField()
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.name + self.dics.name
class pha_loc(models.Model):
    doc = models.ForeignKey(pharmacy, on_delete=models.CASCADE, related_name="pha_loc")
    clinic_add = models.TextField(max_length=300)

    def __str__(self):
        return  self.doc.name
class pha_buss(models.Model):
    doc1 = models.OneToOneField(pharmacy, on_delete=models.CASCADE, primary_key=True, related_name="pha_buss")
    dates = models.DateField()

    def __str__(self):
        return self.doc1.name
class pha_product(models.Model):
        doc = models.ForeignKey(pharmacy,null=True, on_delete=models.CASCADE, related_name="pha_product")
        img = models.ImageField()
        name = models.CharField(max_length=200)
        about = models.TextField(max_length=1000)
        manufacture_company_name= models.CharField(max_length=500)
        price=models.IntegerField()
        desc = models.TextField(max_length=1000)
        dire_for_use=models.TextField(max_length=500)
        storage = models.TextField(max_length=500)
        admin_instruction = models.TextField(max_length=500)
        warning = models.TextField(max_length=500)
        precaution = models.TextField(max_length=500)
        categorie=models.CharField(max_length=100)
        quntity=models.IntegerField(default=0)
        expiry_date=models.DateField(blank=True,null=True)
        created_date=models.DateTimeField(auto_now=True)
        discount=models.IntegerField(default=0)
        genatic_name=models.CharField(blank=True,max_length=20)
        def __str__(self):
            return self.name
class pha_apply(models.Model):
    doc = models.ForeignKey(pha_product, on_delete=models.CASCADE, related_name="pha_apply")
    applied_for = models.TextField(max_length=100)

    def __str__(self):
        return self.doc.name+self.doc.doc.name
class pha_highlight(models.Model):
    doc = models.ForeignKey(pha_product, on_delete=models.CASCADE, related_name="pha_highlight")
    des = models.TextField(max_length=100)

    def __str__(self):
            return self.doc.name+self.doc.doc.name
class product_cart(models.Model):
    user_id=models.IntegerField()
    product_id = models.IntegerField()
    pharmacy_name = models.CharField(max_length=60)
    Sku_no = models.IntegerField()
    quntity = models.IntegerField()

    def __str__(self):
        return self.pharmacy_name
class pharmacy_prod_order(models.Model):
    username=models.CharField(max_length=40)
    phone=models.IntegerField()
    address=models.TextField(max_length=50)
    shipping_details=models.TextField(max_length=50,blank=True)
    card_name=models.CharField(max_length=50)
    card_no=models.IntegerField()
    cvv=models.IntegerField()
    exp_month=models.DateField()
    exp_year=models.DateField()
    product_id = models.ForeignKey(pha_product,related_name='order',on_delete=models.CASCADE)
    pharmacys = models.ForeignKey(pharmacy,related_name='orders',default=True,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    quntitys = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    product_name=models.CharField(max_length=40,blank=True)
    payment_status=models.CharField(max_length=30)
    invoice=models.IntegerField()
    supply=models.ForeignKey('Admin_pharmacy.supplier',null=True,related_name='supp',on_delete=models.CASCADE)
    def __str__(self):
        return self.username+self.product_name








