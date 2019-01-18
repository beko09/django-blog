from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import come2_form
from .models import come2,info
from django.contrib.auth.models import User
# Register your models here.
def index(request):
    return render(request,'base.html',{})
def reg(request):
    form1=come2_form(request.POST or None)#register data
    ob=come2()
    if form1.is_valid():
        if not form1.cleaned_data['birthday']:
            ob.birthday='1990-4-5'
        else:
            ob.birthday = form1.cleaned_data['birthday']
        ob.name=form1.cleaned_data['name']
        ob.email=form1.cleaned_data['email']
        ob.age=form1.cleaned_data['age']

        ob.save()
        return render(request,'base.html',{})
    return render(request,'come2_form.html',{'f':form1})
###############################################################
## Register##
def register(request):
    return render(request,'register.html',{})
def register_backend(request):
    try:
        new = User.objects.create_user(request.POST['user_name'], request.POST['email_user'], request.POST['Password'])
        new.first_name = request.POST['first_name']
        new.last_name = request.POST['last_name']
        new.save()
    except:
        return  HttpResponse('user is exit')

    return HttpResponseRedirect('/beko33')

###############################################################
## login in ###########

def log(request):
    return render(request,'login.html',{})
def log_backend(request):
    u = request.POST['user_name']
    p=request.POST['Password']
    re= authenticate(username=u, password=p)
    if re is not None :
        login(request,re)
        link='/beko33/profile/'+ str(re)
        return HttpResponseRedirect(link)
    else:
        return HttpResponse('no it')

###############################################################
#pro file###################

def profile(request,username):
    return render(request,'profile.html',{'u':username})


###############################################################
#logout

def logout_backend(request):
    logout(request)
    return  HttpResponse('logout')

def info(request,username):
    return render(request,"info.html",{'username':username})

def infoback(request,username):
    u = info()
    user = User.objects.get(username=username)
    u.job = request.POST['job']
    u.lang = request.POST['lang']
    u.num = request.POST['num']
    u.username = user
    u.save()
    return HttpResponse('yes saved')

def beko(request):
    return HttpResponse("helo to sublime text")

