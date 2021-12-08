from django.db import models

# Create your models here.
from doctors.models import Dr


class Newsletter_subscriber(models.Model):
    suscriber_email=models.EmailField()

    def __str__(self):
        return self.suscriber_email

class dr_blogs(models.Model):
    doc = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name="dr_bilogs")
    title = models.CharField(max_length=3000)
    desc = models.TextField(max_length=10000)
    date = models.DateField()
    img = models.ImageField(null=True)

    def __str__(self):
        return self.title + self.doc.name