from django.urls import path
from  .views import page1,page2,page3,form,formupdate,backend,Delte,slect

urlpatterns=[
    path('',page1,name='index'),
    path('page2', page2, name='2'),
    path('page3', page3, name='3'),
    path('form', form, name='4'),
    path('formupdate/<int:id>/', formupdate, name='formupdate'),
    path('backend/<int:id>/', backend, name='backend'),
    path('Delte/<int:id>/', Delte, name='Delte'),
    path('slect', slect, name='slect'),


]