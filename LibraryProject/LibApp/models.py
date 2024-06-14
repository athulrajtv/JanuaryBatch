from django.db import models

# Create your models here.

class LibraryDB(models.Model):
    BookID = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=50)
    AuthorName = models.CharField(max_length=50)
    Pub_Date = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Image = models.CharField(max_length=100)