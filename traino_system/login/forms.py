from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class createAccount(UserCreationForm):
    is_Admin= models.BooleanField(default= False)
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1','password2', 'is_staff']