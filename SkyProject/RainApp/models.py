from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=40,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(max_length=40,null=True,blank=True)


class Category2DB(models.Model):
    CategoryName = models.CharField(max_length=40,null=True,blank=True)
    Product_Name = models.CharField(max_length=40,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(max_length=40,null=True,blank=True)
