from django.db import models

# Create your models here.
class come(models.Model):#name of class mean name of table
    fullname=models.CharField(max_length=100) # name of varbile mean name of virtal
    email=models.EmailField() #email
    age=models.IntegerField()
    birthday=models.DateField()
    def __str__(self):
        return self.fullname