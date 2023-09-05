from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDB
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def indexpage(req):
    return render(req,"Index.html")
def addcategory(req):
    return render(req,"AddCategory.html")
def savecat(req):
    if req.method=="POST":
        na = req.POST.get("name")
        ds = req.POST.get("description")
        im = req.FILES["image"]
        obj = CategoryDB(Category_Name=na, Description=ds, Image=im)
        obj.save()
        messages.success(req, "Product Saved Successfully")
        return redirect(addcategory)
def displaycategory(req):
    data = CategoryDB.objects.all()
    return render(req,"DisplayCategory.html",{"data":data})
def editcategory(req,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(req,"EditCategory.html",{"data":data})
def updatecategory(req,dataid):
    if req.method == "POST":
        na = req.POST.get("name")
        ds = req.POST.get("description")
        try:
            img = req.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(Category_Name=na,Description=ds,Image=file)
        messages.success(req, "Data Updated")
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.error(req, "Data Deleted")
    return redirect(displaycategory)


def addproduct(req):
    data = CategoryDB.objects.all()
    return render(req,"AddProduct.html",{"data":data})
def savepdt(req):
    if req.method == "POST":
        ca = req.POST.get("cate")
        pn = req.POST.get("name")
        qt = req.POST.get("quantity")
        pr = req.POST.get("price")
        ds = req.POST.get("description")
        im = req.FILES["image"]
        obj = ProductDB(CategoryName=ca, ProductName=pn, Quantity=qt, Price=pr, Description=ds, Image=im)
        obj.save()
        messages.success(req, "Product Saved Successfully")
        return redirect(addproduct)
def displayproduct(req):
    data = ProductDB.objects.all()
    return render(req,"DisplayProduct.html",{"data":data})
def editproduct(req,dataid):
    data = ProductDB.objects.get(id=dataid)
    da = CategoryDB.objects.all()
    return render(req,"EditProduct.html",{"da":da, "data":data})
def updateproduct(req,dataid):
    if req.method=="POST":
        ca = req.POST.get("cate")
        pn = req.POST.get("name")
        qt = req.POST.get("quantity")
        pr = req.POST.get("price")
        ds = req.POST.get("description")
        try:
            img = req.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).Image
        ProductDB.objects.filter(id=dataid).update(CategoryName=ca,ProductName=pn,Quantity=qt,Price=pr,Description=ds,Image=file)
        messages.success(req, "Data Updated")
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Data Deleted")
    return redirect(displayproduct)
def adminlogin(request):
    return render(request,"AdminLogin.html")
def save_admin(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('password')
        if User.objects.filter(username__contains=a).exists():
            user = authenticate(username=a, password=b)
            if user is not None:
                login(request, user)
                request.session['username'] = a
                request.session['password'] = b
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)