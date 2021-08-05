from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"templates/base.html")
def home(request):
    return render(request,"templates/home.html")
def events(request):
    return render(request,"templates/event.html")
def about(request):
    return render(request,"templates/about.html")
def contact(request):
    return render(request,"templates/contact.html")
