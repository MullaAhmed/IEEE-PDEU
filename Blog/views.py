from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request,"blog_home.html")
def blog_page(request):
    return render(request,"page.html")

def page1(request):
    return render(request,"Page1.html")
def page2(request):
    return render(request,"Page2.html")
def page3(request):
    return render(request,"Page3.html")
def page4(request):
    return render(request,"Page4.html")
def page5(request):
    return render(request,"Page5.html")
