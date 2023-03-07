from django.shortcuts import render
from .models import  Post


posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]


def siteblog(request):
    posts=Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'siteblog/home.html',context)


def details(request):
    return render(request, "setblog/about.html")
