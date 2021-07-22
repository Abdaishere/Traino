from django.core.checks import messages
import customer
from django.db.models.fields import CharField
from customer.models import Customer
from adminn.models import Train
from django.db import models
from datetime import date
class Trip(models.Model):
    source=models.CharField(max_length=20)
    destination= models.CharField(max_length=20)
    is_available=models.BooleanField(default=True)
    available_seat= models.IntegerField()
    ticket_price = models.IntegerField()
    trip_number = models.IntegerField()
    trip_date = models.DateField(auto_now=False, auto_now_add=False)
    trip_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    train= models.ForeignKey(Train,on_delete=models.CASCADE)
    def __str__(self) :
        return "Trip number" + str(self.id)

class Booking(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)
    trip_number=models.ForeignKey(Trip,on_delete=models.CASCADE)    
    train_num= models.ForeignKey(Train,on_delete=models.CASCADE)
    seat_number=models.IntegerField()
    full_name=models.CharField(max_length=200)
    def __str__(self) :
        return "Booking id" + str(self.id)

class Visa (models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    visa_name=models.CharField(max_length=250)
    card_number=models.IntegerField()
    date_card=models.DateField(auto_now=False, auto_now_add=False)
    cvc=models.CharField(max_length=3)
    def __str__(self) :
        return str(self.id)
    

class fawary(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    fawary_name=models.CharField(max_length=250)
    fawary_email=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    def __str__(self) :
        return str(self.id)