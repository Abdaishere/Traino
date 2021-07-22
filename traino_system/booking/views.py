from typing import FrozenSet
from customer.models import Customer
from django.db.models import query
from booking.forms import TripForm
from booking.models import Trip,Booking,Visa,fawary
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import datetime
def home(request):
    if request.method=="GET":
        return render(request,'booking/home.html',{})
    else:
        trip_date=request.POST.get('trip_date',False)
        source=request.POST.get('source',False)
        destination=request.POST.get('destination',False)
        request.session['trip_date']=trip_date
        request.session['source']=source
        request.session['destination']=destination
        data=Trip.objects.filter(source=source,destination=destination,is_available=True,trip_date=trip_date)
        return render(request,'booking/show.html',{'data':data})

"""def show_booking(request):
    if request.method=="POST":
        form=TripForm(request.POST)
        return HttpResponse("HELLO,world")
        #setquery=Trip.objects.filter()
        #form.save()
    else:
        form=TripForm()
    return render(request,'booking/show.html',{'form':form})"""
"""def show_booking(request):
    if request.POST == 'POST':
        date=request.POST['tripd']
        return HttpResponse(date)
    else:
        date=request.GET['tripd']
        return HttpResponse(date)
"""
def show_booking(request):
    data = {}
    if request.method=="GET":
        return render(request,'booking/home.html',{"data":data})
    else:
        trip_date=request.POST.get('trip_date',False)
        source=request.POST.get('source',False)
        destination=request.POST.get('destination',False)
        request.session['trip_date']=trip_date
        request.session['source']=source
        request.session['destination']=destination
        data=Trip.objects.filter(source=source,destination=destination,is_available=True,trip_date=trip_date)
        return render(request,'booking/show.html',{'data':data})
def book(request,id):
    if request.session.get("email",None) and request.session.get("type",None)=='customer':
        request.session['trip_number']=id
        return render(request,'booking/book.html')
    else:
        next="book/"+id
        return redirect('home')
def visa(request):
    if request.session.get("email",None) and request.session.get("type",None)=='customer':
        if request.method=='POST':
            fullname=request.POST['full_name']
            request.session['full_name']=fullname
            return render(request,'booking/visa.html')
        else:
            messages.info(request,"Empty field of Fullname")
            return redirect('book')
    else:
        redirect('home')
def fawaryy(request):
    if request.session.get("email",None) and request.session.get("type",None)=='customer':
        if request.method=='POST':
            fullname=request.POST['full_name']
            request.session['full_name']=fullname
            return render(request,'booking/f.html')
        else:
            messages.info(request,"Empty field of Fullname")
            return redirect('book')
    else:
        redirect('home')

def inside_visa(request):   
    if request.method=='POST':
        visa_name=request.POST['visa_name']
        card_number=request.POST['card_number']
        date_card=request.POST['card_number']
        cvc=request.POST['cvc']
        request.session['visa_name']=visa_name
        request.session['card_number']=card_number
        request.session['date_card']=date_card
        request.session['cvc']=cvc
        return render(request,'booking/book.html')
    else:
        messages.info(request,"Empty fields")
        return redirect('book')

def inside_fawary(request):
    if request.method=='POST':
        fawary_name=request.POST['fawary_name']
        fawary_email=request.POST['fawary_email']
        phone_number=request.POST['phone_number']
        request.session['fawary_name']=fawary_name
        request.session['fawary_email']=fawary_email
        request.session['phone_number']=phone_number
        return render(request,'booking/book.html')
    else:
        messages.info(request,"Empty fields")
        return redirect('book')

def book_confirm(request):
    fullname=request.session['full_name']
    trip_number=request.session['trip_number']
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    trip=Trip.objects.get(trip_number=trip_number)
    seat_number = trip.available_seat
    trip.available_seat= trip.available_seat -1
    if(trip.available_seat ==0):
        trip.is_available=False
    train= trip.train
    trip.save()
    data=Booking(customer=customer,trip_number=trip_number,train=train,seat_number=seat_number)
    data.save()
    del request.session['full_name']
    del request.session['trip_number']
    messages.info(request,"Trip has been successfully booked")
    return redirect('user_dashboard')
def cancel_trip(request,id):
    data=Booking.objects.get(id=id)
    trip=data.trip_number
    if trip.available_seat ==0:
        trip.is_available=True
    trip.available_seat = trip.available_seat +1
    trip.save() 
    data.delete()
    return HttpResponse("Booking Cancelled Successfully")