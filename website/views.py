from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def base(response):
    return render(response,"base.html")
def home(response):
    return render(response,"home.html")
def events(response):
    form=event_contact(response.POST)

    if form.is_valid():
        n=form.cleaned_data["text"]
        i=form.cleaned_data["text"]
        t=form.cleaned_data["text"]
        a=Event(name=n,info=i,text=t)
        a.save()
    return render(response,"event.html",{"form":form})

def about(response):
    return render(response,"about.html")
def contact(response):
    return render(response,"contact.html")
def team(response):
    return render(response,"team.html")
def creators(response):
    return render(response,"creators.html")

