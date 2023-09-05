from django.db import models

# Create your models here.

class CartDB(models.Model):
    Name = models.CharField(max_length=40,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    User = models.CharField(max_length=40, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)



class CheckoutDB(models.Model):
    FullName = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=40,null=True,blank=True)
    State = models.CharField(max_length=40,null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    Town = models.CharField(max_length=50,null=True,blank=True)
    Landmark = models.CharField(max_length=50,null=True,blank=True)
    Pincode = models.CharField(max_length=50,null=True,blank=True)
    PhoneNumber = models.CharField(max_length=50,null=True,blank=True)

class UserDB(models.Model):
    Username = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Password = models.CharField(max_length=40,null=True,blank=True)
    Con_Password = models.CharField(max_length=40,null=True,blank=True)