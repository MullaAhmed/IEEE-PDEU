from django.urls import path
from . import views

urlpatterns = [
    
    path('blog/',views.blog_home,name='Blog Home'),
    path('blog/page/',views.blog_page,name='Page'),
]