from django.urls import path
from . import views

urlpatterns = [
    
    path('blog/',views.blog_home,name='Blog Home'),
    path('blog/page/',views.blog_page,name='Page'),

    path('blog/page1/',views.page1,name="page1"),
    path('blog/page2/',views.page2,name="page2"),
    path('blog/page3/',views.page3,name="page3"),
    path('blog/page4/',views.page4,name="page4"),
    path('blog/page5/',views.page5,name="page5"),
]