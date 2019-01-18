from django.shortcuts import render
from .import models
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def page1(request):
    a = {"b": "abobaker", "a": "hilal", "c": "ahemd","l":[1,23,4,4,5,5]}
    data = models.come.objects.all()
    return render(request, 'base.html', {'d': data})

def page2(request):
    return render(request,'page2.html',{})
#page creat two function
def page3(request):

    return render(request,'page3.html',{})


def form(request):
    new = models.come(fullname=request.POST['name'],email=request.POST['email'],age= request.POST['age'],birthday=request.POST['date'])
    new.save()
    return HttpResponseRedirect('/bekosite2/')
#end function creat

#page of update two function
def formupdate(request,id):
    #data=models.come.objects.all()#all()[5:]
    data = models.come.objects.filter(age__gt=6)#id=id,fullname='hhhh',age__in=[6,80],id=1,age=67,gt mean < ,gte mean = ,lt mean >
    #data = models.come.objects.get(id=id)
    #data=models.come.objects.order_by('age')#order data by argment
    print(str(data))
    #return render(request,'formupdate.html',{'idform':id,'data':data[id-1]})
    return render(request,'formupdate.html',{'idform':id,'data':data[0]})#data
    #return render(request,'formupdate.html',{'idform':id,'data':data})

def backend(request,id):
    new= models.come(id=id,fullname=request.POST['name'], email=request.POST['email'], age=request.POST['age'],
                      birthday=request.POST['date'])
    new.save()
    return HttpResponseRedirect('/bekosite2/')
#end function update

#delte function only
def Delte(request,id):
    old=models.come(id=id)
    old.delete()
    return  HttpResponseRedirect('/bekosite2/')
#end delte

#slect function
def slect(request):
    data=models.come.objects.all()
    return render(request,'base.html',{'d':data})