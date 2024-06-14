from django.conf.urls import url
from LibApp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^Librarypage/', views.LibraryAPI),
    url(r'Librarypage/([0-9]+)$', views.LibraryAPI),
    url(r'^imagepage$',views.savefile),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)