from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import post

# Create your views here.
def base(request):
    return render(request,'base.html',{})
def home(request):
    context = {
        'post': post.objects.all()
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html',{'title':'about'})
def arictle(request):
    context = {
        'post': post.objects.all()
    }
    return render(request,'arictle.html',context)
