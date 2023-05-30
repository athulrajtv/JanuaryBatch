from django.shortcuts import render,redirect
from JerryApp.models import CategoryDB,Category2DB
from WebApp.models import CartDB,UserDB,CheckoutDB
from django.contrib import messages
# Create your views here.

def homepage(req):
    data = CategoryDB.objects.all()
    return render(req,"home.html",{"data":data})
def productpage1(req):
    return render(req,"Products.html")
def productpage(req,catg):
    pro = Category2DB.objects.filter(CategoryName=catg)
    return render(req,"Products.html",{"pro":pro})

def checkoutpage(req,dataid):
    data = Category2DB.objects.get(id=dataid)
    return render(req,"Check.html",{"data":data})

def savecart(req):
    if req.method=="POST":
        na = req.POST.get("name")
        pr = req.POST.get("price")
        qt = req.POST.get("qty")
        us = req.POST.get("user")
        obj = CartDB(Name=na,Price=pr,Quantity=qt,User=us)
        obj.save()
        messages.success(req,"Product Saved Successfully")
        return redirect(homepage)
def DeleteItem(req,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycart)
def userpage(req):
    return render(req,"Userlogin.html")
def saveuser(req):
    if req.method == "POST":
        us = req.POST.get("name")
        em = req.POST.get("email")
        ps = req.POST.get("password")
        cps = req.POST.get("cpassword")
        obj = UserDB(Username=us,Email=em,Password=ps,Con_Password=cps)
        obj.save()
        return redirect(userpage)
def userlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if UserDB.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            return redirect(homepage)
        else:
            return redirect(userpage)
    return redirect(userpage)
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userlogin)

def displaycart(req):
    cat = CartDB.objects.filter(User=req.session['username'])
    return render(req,"cart.html",{"cat":cat})
def checkpage(req):
    return render(req,"checkout.html")
def savecheck(req):
    if req.method == "POST":
        fn = req.POST.get("name")
        em = req.POST.get("email")
        st = req.POST.get("state")
        ad = req.POST.get("address")
        tw = req.POST.get("town")
        lm = req.POST.get("mark")
        pc = req.POST.get("pin")
        pn = req.POST.get("number")
        obj = CheckoutDB(FullName=fn,Email=em,State=st,Address=ad,Town=tw,Landmark=lm,Pincode=pc,PhoneNumber=pn)
        obj.save()
        return redirect(checkpage)
