from django.urls import path
from AdminApp import views


urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecat/',views.savecat,name="savecat"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),

    path('addproduct/',views.addproduct,name="addproduct"),
    path('savepdt/',views.savepdt,name="savepdt"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('save_admin/',views.save_admin,name="save_admin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('Admin_Logout/',views.Admin_Logout,name="Admin_Logout"),
]