#from booking.models import Trip
from django.db import models

class Train(models.Model):
    train_number=models.IntegerField()
    number_of_trips=models.IntegerField()
    number_of_seats= models.IntegerField()
    train_driver=models.CharField(max_length=50)
    #trip= models.ForeignKey(Trip,on_delete=models.CASCADE,default=None)
    def __str__(self) :
        return "Train number" + str(self.id)

class Admin(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    phone=models.IntegerField()
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    password= models.CharField(max_length=50)
    access_code=models.CharField(max_length=4)
    #image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    def __str__(self):
        return "Admin ID: "+str(self.id)
