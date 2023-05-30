from django.urls import path
from WebApp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('productpage1/', views.productpage1, name="productpage1"),
    path('productpage/<catg>/', views.productpage, name="productpage"),
    path('checkoutpage/<int:dataid>/', views.checkoutpage, name="checkoutpage"),

    path('savecart/', views.savecart, name="savecart"),
    path('userpage/', views.userpage, name="userpage"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('displaycart/', views.displaycart, name="displaycart"),
    path('Admin_Logout/', views.Admin_Logout, name="Admin_Logout"),
    path('checkpage/', views.checkpage, name="checkpage"),
    path('savecheck/', views.savecheck, name="savecheck"),
    path('DeleteItem/<int:dataid>/', views.DeleteItem, name="DeleteItem"),
]