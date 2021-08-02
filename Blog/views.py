from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request,"/Blog/blog_home.html")
def blog_page(request):
    return render(request,"/Blog/page.html")
