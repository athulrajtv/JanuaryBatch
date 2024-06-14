from django.urls import path
from RawApp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('brandpage/<catg>/', views.brandpage, name="brandpage"),
    path('brandpage1', views.brandpage1, name="brandpage1"),
    path('specialpage/<det>/', views.specialpage, name="specialpage"),
    path('contactpage', views.contactpage, name="contactpage"),


]