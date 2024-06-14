from django.urls import path
from RainApp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategorypage/',views.addcategorypage,name="addcategorypage"),
    path('savecat/',views.savecat,name="savecat"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('categorydisplay/', views.categorydisplay, name="categorydisplay"),
    path('savecate/', views.savecate, name="savecate"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('categoryedit/<int:dataid>/', views.categoryedit, name="categoryedit"),
    path('categoryupdate/<int:dataid>/', views.categoryupdate, name="categoryupdate"),
    path('categorydelete/<int:dataid>/', views.categorydelete, name="categorydelete"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('Admin_Logout/', views.Admin_Logout, name="Admin_Logout"),

]