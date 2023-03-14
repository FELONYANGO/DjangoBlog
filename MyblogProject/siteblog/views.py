from django.shortcuts import render,redirect
from .models import  Post
from .forms import PostForm


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
def create_post(request):
    if request.method =='GET':
        context = {'forms':PostForm(request.POST)}
        return render(request, 'siteblog/post_form.html', context)
    
    elif request.method =='POST':
        form  = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
        else:
            return render(request, 'siteblog/post_form.html', {'form': form})
        
