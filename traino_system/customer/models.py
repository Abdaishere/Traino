from django.db import models
from django.urls.conf import path

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    phone=models.IntegerField()
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    password= models.CharField(max_length=50)
    #image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    def __str__(self):
        return "Customer ID: "+str(self.id)

# Create your models here.
