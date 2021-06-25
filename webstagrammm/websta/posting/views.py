from django.shortcuts import render,redirect
from .models import post
from django.contrib.auth.models import User
# Create your views here.
def feed(request):
    posts = post.objects.all()
    return render(request,'feed.html',{'posts':posts})

def profile(request):
    posts = post.objects.all()
    return render(request,'profile.html',{'posts':posts})

def new(request):
    return render(request,'new.html')

def create(request):
    new_post = post()
    new_post.user = request.user
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('feed')

def edit(request,id):
    edit_post = post.objects.get(id=id)
    return render(request,'edit.html',{'post':edit_post})

def update(request, id):
    update_post = post.objects.get(id=id)
    update_post.user = request.user
    update_post.image = request.FILES['image']
    update_post.save()

    return redirect('feed')

def delete(request,id):
    delete_post = post.objects.get(id=id)
    delete_post.delete()
    return redirect ('feed') 