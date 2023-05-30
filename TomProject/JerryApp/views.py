from django.shortcuts import render,redirect
from JerryApp.models import CategoryDB,Category2DB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def indexpage(req):
    return render(req,"index.html")
def addcategory(req):
    return render(req,"AddCategory.html")
def savecat(req):
    if req.method=="POST":
        na = req.POST.get("name")
        ds = req.POST.get("description")
        im = req.FILES["image"]
        obj = CategoryDB(Category_Name=na,Description=ds,Image=im)
        obj.save()
        messages.success(req,"Product Saved Successfully")
        return redirect(addcategory)
def displaycategory(req):
    data = CategoryDB.objects.all()
    return render(req,"Displaycategory.html",{"data":data})
def editcategory(req,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(req,"Editcategory.html",{"data":data})
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





def productpage(req):
    data = CategoryDB.objects.all()
    return render(req,"product.html",{"data":data})
def savecate(req):
    if req.method=="POST":
        ca = req.POST.get("cate")
        pn = req.POST.get("name")
        qt = req.POST.get("quantity")
        pr = req.POST.get("price")
        ds = req.POST.get("description")
        im = req.FILES["image"]
        obj = Category2DB(CategoryName=ca,Product_Name=pn,Quantity=qt,Price=pr,Description=ds,Image=im)
        obj.save()
        return redirect(productpage)
def displayproduct(req):
    data = Category2DB.objects.all()
    return render(req, "Displayproduct.html",{"data":data})
def editproduct(req,dataid):
    data = Category2DB.objects.get(id=dataid)
    da = CategoryDB.objects.all()
    messages.success(req, "Product Updated")
    return render(req,"Editproduct.html",{"data":data, "da":da})
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
            file = Category2DB.objects.get(id=dataid).Image
        Category2DB.objects.filter(id=dataid).update(CategoryName=ca,Product_Name=pn,Quantity=qt,Price=pr,Description=ds,Image=file)
        messages.success(req, "Product Saved Successful")
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = Category2DB.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Data Deleted")
    return redirect(displayproduct)

def adminpage(request):
    return render(request,"Login.html")
def Admin_Login(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r,password = password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexpage)
            else:
                return redirect(adminpage)
        else:
            return redirect(adminpage)
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminpage)
