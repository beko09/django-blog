from django.urls import path
from .views import index,reg,register,register_backend,log,log_backend,profile,logout_backend,info,infoback,beko
urlpatterns = [
    path('',index,name='index'),
    path('reg/',reg,name='reg'),
    path('register/',register,name='register'),
    path('register_backend',register_backend,name='register_backend'),
    path('log/', log, name='log'),
    path('log_backend', log_backend, name='log_backend'),
    path('profile/<str:username>/',profile,name='profile'),
    path('logout_backend',logout_backend,name='logout_backend'),
    path('info/<str:username>/',info,name='info'),
    path('infoback/<str:username>/',infoback,name='infoback'),
    path('beko/',beko),
]