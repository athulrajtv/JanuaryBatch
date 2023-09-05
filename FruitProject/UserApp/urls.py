from django.urls import path
from UserApp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('productpage/<catg>/', views.productpage, name="productpage"),
    path('singleproduct/<int:dataid>/', views.singleproduct, name="singleproduct"),
    path('savecart/', views.savecart, name="savecart"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('DeleteItem/<int:dataid>/', views.DeleteItem, name="DeleteItem"),
    path('placeorder/', views.placeorder, name="placeorder"),
    path('savecheck/', views.savecheck, name="savecheck"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('Admin_Logout/', views.Admin_Logout, name="Admin_Logout"),
]
