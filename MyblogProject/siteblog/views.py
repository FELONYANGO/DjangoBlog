from django.shortcuts import render,redirect,get_object_or_404
from .models import  Post
from django.contrib import messages
from .forms import PostForm



def edit_post(request,id):
    edit=get_object_or_404(Post,id)
    if request.method == 'Get':
        context={'form':PostForm(instance=edit),'id':id}

        return render(request,'siteblog/post_form.html',context)

    


def create_post(request):
    if request.method =='GET':
        context = {'forms':PostForm(request.POST)}
        return render(request, 'siteblog/post_form.html', context)
    
    elif request.method =='POST':
        form  = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"you have successfully created your posts")
            return redirect('siteblog')
        else:
            messages.error(request,'there seem to be an error in your entry')
            return render(request, 'siteblog/post_form.html', {'form': form})
def siteblog(request):
    posts=Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'siteblog/home.html',context)


def details(request):
    return render(request, "setblog/about.html")

        
