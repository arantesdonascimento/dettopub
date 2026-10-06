from django.urls import path
from . import views



urlpatterns = [

    path('', views.blogs, name='blogs'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('create/', views.blog_create, name='blog_create'),
    
]