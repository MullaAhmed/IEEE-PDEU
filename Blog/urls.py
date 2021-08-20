from django.urls import path
from . import views

urlpatterns = [
    
    #Latest one should be named blog home1
    #Latest should also have the address 
    path('blog1/',views.blog_home_1,name='Blog Home2'),

    path('blog1/page1.1/',views.page1_1,name="page1.1"),
    path('blog1/page1.2/',views.page1_2,name="page1.2"),
    path('blog1/page1.3/',views.page1_3,name="page1.3"),
    path('blog1/page1.4/',views.page1_4,name="page1.4"),
    path('blog1/page1.5/',views.page1_5,name="page1.5"),
    path('blog1/page1.6/',views.page1_6,name="page1.6"),

    path('blog2/',views.blog_home_2,name='Blog Home1'),
    path('blog2/page2.1/',views.page2_1,name="page2.1"),
    path('blog2/page2.2/',views.page2_2,name="page2.2"),
    path('blog2/page2.3/',views.page2_3,name="page2.3"),
]