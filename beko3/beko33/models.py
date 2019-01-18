from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class come2(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      age=models.IntegerField()
      birthday=models.DateField()
      hh=models.CharField(max_length=50)
      def __str__(self):
          return self.name,self.email

class info(models.Model):
      username = models.ForeignKey(User,on_delete=models.CASCADE)
      job = models.CharField(max_length=100)
      lang = models.CharField(max_length=100)
      num = models.IntegerField()


