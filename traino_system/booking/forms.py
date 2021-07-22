from django.forms import ModelForm, fields

from .models import Trip,Booking,Visa,fawary
from booking import models

class TripForm(ModelForm):
    class Meta:
        model = Trip 
        fields ='__all__'
        