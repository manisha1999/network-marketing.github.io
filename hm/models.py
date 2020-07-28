from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    email = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    msg = models.CharField(max_length=500, default="")

class Join(models.Model):
    mobn = models.CharField(max_length=10)
    fname = models.CharField(max_length=50)
    spid = models. CharField(max_length=50)
    lname= models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    state =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50,default="")



