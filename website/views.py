from django.shortcuts import render

# Create your views here.
def base(response):
    return render(response,"base.html")
def home(response):
    return render(response,"home.html")
def events(response):
    return render(response,"event.html")
def about(response):
    return render(response,"about.html")
def contact(response):
    return render(response,"contact.html")
def team(response):
    return render(response,"team.html")
def creators(response):
    return render(response,"creators.html")