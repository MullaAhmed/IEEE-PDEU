from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    #path('base/',views.base,name='base'),
    path('events/',views.events,name='events'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    
]
