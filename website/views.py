from django.shortcuts import render

# Create your views here.
def base(response):
    return render(response,"/website/base.html")
def home(response):
    return render(response,"/website/home.html")
def events(response):
    return render(response,"/website/event.html")
def about(response):
    return render(response,"/website/about.html")
def contact(response):
    return render(response,"/website/contact.html")
