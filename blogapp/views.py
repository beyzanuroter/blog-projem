from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Blogapp,Category

def index(request):
    context = {
        "blogs": Blogapp.objects.filter(is_active=True,is_home=True),
        "categories": Category.objects.all()
    }
    return render (request, "blogapp/index.html",context)

def blogs(request):
    context = {
        "blogs": Blogapp.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request,"blogapp/blogs.html",context)

def blog_details(request, slug):
    blog = Blogapp.objects.get(slug=slug)
    return render(request, "blogapp/blog-details.html", {
        "blog":blog
    })

def blogs_by_category(request, slug):
     context = {
         "blogs": Category.objects.get(slug=slug).blogapp_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug 
    }
     return render(request,"blogapp/blogs.html",context)
    
