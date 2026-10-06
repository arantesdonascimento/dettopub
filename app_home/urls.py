from django.urls import path
from . import views



urlpatterns = [

	path('base/', views.BASE, name='base'),
    path('', views.home, name='home'),
    path('rolunk/', views.about, name='about'),
    path('kapcsolat/', views.contact, name='contact'),
    path('teremberles/', views.teremberles, name='teremberles'),
    path('esemenyek/', views.esemenyek, name='esemenyek'),
    path('galeria/', views.gallery, name='gallery'),
    path('arak/', views.pricing, name='pricing'),
]