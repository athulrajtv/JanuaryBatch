from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDB
from UserApp.models import CartDB,CheckoutDB,UserDB
from django.contrib import messages


# Create your views here.

def homepage(req):
    data = CategoryDB.objects.all()
    da = ProductDB.objects.all()
    return render(req,"HomePage.html",{"data":data, "da":da})
def productpage(req,catg):
    pro = ProductDB.objects.filter(CategoryName=catg)
    return render(req,"ProductPage.html",{"pro":pro})
def singleproduct(req,dataid):
    data = ProductDB.objects.get(id=dataid)
    return render(req,"SingleProduct.html",{"data":data})
def savecart(req):
    if req.method == "POST":
        na = req.POST.get("name")
        pr = req.POST.get("price")
        qt = req.POST.get("qty")
        us = req.POST.get("user")
        tp = req.POST.get("tprice")
        obj = CartDB(Name=na,Price=pr,Quantity=qt,User=us,TotalPrice=tp)
        obj.save()
        messages.success(req, "Item Add To The Cart")
        return redirect(homepage)
def cartpage(req):
    item = CartDB.objects.filter(User=req.session['username'])
    return render(req,"Cart.html",{"item":item})
def DeleteItem(req,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    messages.error(req, "Data Deleted")
    return redirect(cartpage)
def placeorder(req):
    item = CartDB.objects.filter(User=req.session['username'])
    total_price = 0
    for i in item:
        total_price = total_price + i.TotalPrice
    return render(req,"PlaceOrder.html",{"item":item,"total_price":total_price})
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
        messages.success(req, "Order Placed Successfully")
        return redirect(placeorder)

def userloginpage(req):
    return render(req,"UserLogin.html")
def saveuser(req):
    if req.method == "POST":
        us = req.POST.get("name")
        em = req.POST.get("email")
        ps = req.POST.get("password")
        cps = req.POST.get("cpassword")
        obj = UserDB(Username=us,Email=em,Password=ps,Con_Password=cps)
        obj.save()
        return redirect(userloginpage)
def userlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if UserDB.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            messages.success(request, "Login Successful")
            return redirect(homepage)
        else:
            return redirect(userloginpage)
    return redirect(userloginpage)
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userloginpage)
