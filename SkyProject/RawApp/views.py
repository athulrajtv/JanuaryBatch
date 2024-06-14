from django.shortcuts import render,redirect
from RainApp.models import CategoryDB,Category2DB
from RawApp.models import UserDB
# Create your views here.
def homepage(req):
    data = CategoryDB.objects.all()
    return render(req,"home.html",{"data":data})
def aboutpage(req):
    return render(req,"about.html")
def brandpage(req,catg):
    pro = Category2DB.objects.filter(CategoryName=catg)
    return render(req,"brand.html",{"pro":pro})
def brandpage1(req):
    return render(req,"brand.html")
def specialpage(req,det):
    pro = Category2DB.objects.get(Product_Name=det)
    return render(req,"Special.html",{"pro":pro})
def contactpage(req):
    return render(req,"Contact.html")

