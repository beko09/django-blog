from django.urls import path
from .views import home,about,arictle
from User.views import register,profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',home,name='home'),
    path('arictle',arictle,name='arictle'),
    path('about',about,name='about'),
    path('register', register, name='register'),
    path('log',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile',profile,name='profile'),



]
