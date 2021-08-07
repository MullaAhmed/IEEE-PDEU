from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request,"Blog/blog_home.html")
def blog_page(request):
    return render(request,"Blog/page.html")

def page1(request):
    return render(request,"Blog/Page1.html")
def page2(request):
    return render(request,"Blog/Page2.html")
def page3(request):
    return render(request,"Blog/Page3.html")
def page4(request):
    return render(request,"Blog/Page4.html")
def page5(request):
    return render(request,"Blog/Page5.html")
