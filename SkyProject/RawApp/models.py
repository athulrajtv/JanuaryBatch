from django.db import models

# Create your models here.
class UserDB(models.Model):
    Email = models.CharField(max_length=40,null=True,blank=True)
    Password = models.CharField(max_length=40,null=True,blank=True)
    Password_con = models.CharField(max_length=40,null=True,blank=True)
