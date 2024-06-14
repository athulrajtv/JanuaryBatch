from django.shortcuts import render,redirect
from RainApp.models import CategoryDB,Category2DB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def indexpage(req):
    return render(req,"index.html")
def addcategorypage(req):
    return render(req,"Addcategory.html")
def savecat(req):
    if req.method=="POST":
        na = req.POST.get("name")
        ds = req.POST.get("description")
        im = req.FILES["image"]
        obj = CategoryDB(Category_Name=na,Description=ds,Image=im)
        obj.save()
        return redirect(addcategorypage)
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
        CategoryDB.objects.filter(id=dataid).update(Category_Name=na, Description=ds, Image=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)



def categorydisplay(req):
    data = CategoryDB.objects.all()
    return render(req,"Category.html",{"data":data})
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
        return redirect(categorydisplay)
def categorypage(req):
    data = Category2DB.objects.all()
    return render(req,"CategoryDisplay.html",{"data":data})
def categoryedit(req,dataid):
    data = Category2DB.objects.get(id=dataid)
    da = CategoryDB.objects.all()
    return render(req,"CategoryEdit.html",{"data":data, "da":da})
def categoryupdate(req,dataid):
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
        return redirect(categorypage)
def categorydelete(req,dataid):
    data = Category2DB.objects.filter(id=dataid)
    data.delete()
    return redirect(categorypage)

def adminpage(req):
    return render(req,"login.html")
def admin_login(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
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