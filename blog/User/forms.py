from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  .models import profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="الايميل")
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            "username": "الاسم" ,
            "email":"الايميل",
            "password1":"كلمة السر",
            "password2":"تاكيد كلمة السر",
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'label':'كلمة السر'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),

        }
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="الايميل")

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            "username": "الاسم",
        }
class profileUpdateForm(forms.ModelForm):
    class Meta:
        model= profile
        fields = ['image']
        labels = {
            "image": "الصورة",
        }