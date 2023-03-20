from django.shortcuts import render,redirect,get_object_or_404
from .models import  Post
from django.contrib import messages
from .forms import PostForm



def edit_post(request,id):
    edit=get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context={'form' : PostForm(instance=edit), 'id':id}

        return render(request,'siteblog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            messages.success(request," account updated successfully")
            return redirect('siteblog')
        
        else:
            messages.error(request,"there seem to be an error in your entry")
            return render(request, 'siteblog/post_form.html', {'form': form})
        
def delete_post(request, id):
    delete_post_form = get_object_or_404(Post,pk=id)
    context={'delete_post_form': delete_post_form}

    if request.method == 'GET':
       return render(request, 'siteblog/delete_post.html',context=context)
    
    elif request.method == 'POST':
      delete_post_form.delete()
      messages.seccess(request,'account deleted successfully')
      return redirect('siteblog')


            
    


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

        
