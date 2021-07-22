from booking.models import Trip
from django.http.response import HttpResponse
from login.forms import createAccount
from django.contrib import messages
from adminn.models import Admin, Train
from django.shortcuts import render, resolve_url,redirect

def admin_dashboard(request):
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        data = Train.objects.all()
        return render(request,"adminn/admin_dashboard.html",{"data":data})
    else:
      return redirect("admin_login")
    
def add_train(request):
    if not request.session.get('email',None):
      return redirect('admin_login')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"adminn/addtrain.html",{})
    else:
        train_number=request.POST.get('train_number',False)
        number_of_seats=request.POST.get('number_of_seats',False)
        train_driver=request.POST.get('train_driver',False)
        error=[]
        if(len(train_number)<1):
                error.append(1)
                messages.warning(request,"Train No Field must be atleast 3 digit like 100.")
        if(len(number_of_seats)<1):
            error.append(1)
            messages.warning(request,"Select a valid Seats number")
        if(not len(error)):
            admin=request.session['email']
            manager=Admin.objects.get(email=admin)
            train=Train(train_number=train_number,number_of_trips=0,number_of_seats=number_of_seats,train_driver=train_driver)
            train.save()
            messages.info(request,"Train Added Successfully")
            return redirect('admin_dashboard')
        else:
            return redirect('add_train')

def update_train(request,train_number):
    if not request.session.get('email',None):
      return redirect('admin_login')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    train=Train.objects.get(train_number=train_number)
    if request.method=="GET":
        return render(request,"adminn/updatetrain.html",{"train":train})
    else:
            train_no=request.POST.get('train_number',None)
            train_driver=request.POST.get('train_driver',None)
            error=[]
            if(len(train_no)<=1):
                error.append(1)
                messages.warning(request,"Please enter valid train in 3 digts...")
            if(not len(error)):
                manager=request.session['email']
                manager=Admin.objects.get(email=manager)
                train.train_number=train_no
                train.train_driver=train_driver
                train.save()
                messages.info(request,"Train Data Updated Successfully")
                return redirect('/dashboard1')
            else:
                return redirect('update_train'+train.train_number,{"train":train})

def add_trip(request,id):
    if not request.session.get('email',None):
      return redirect('admin_login')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"adminn/addtrip.html",{})
    else:
        trip_number=request.POST.get('trip_number',False)
        avaliable_seats=request.POST.get('avaliable_seats',False)
        source=request.POST.get('source',False)
        destination=request.POST.get('destination',False)
        trip_data=request.POST.get('trip_data',False)
        trip_time=request.POST.get('trip_time',False)
        ticket_price= request.POST.get('ticket_price',False)
        error=[]
        if(len(trip_number)<1):
                error.append(1)
                messages.warning(request,"Train No Field must be atleast 3 digit like 100.")
        if(len(avaliable_seats)<1):
            error.append(1)
            messages.warning(request,"Select a valid Seats number")
        if(not len(error)):
            #train = Train.objects.filter(id=id)
            trip=Trip(source=source,destination=destination,avaliable_seats=avaliable_seats,trip_number=trip_number,trip_data=trip_data,trip_time=trip_time,ticket_price=ticket_price)
            #train.trip=trip
            trip.save()
            #train.save()
            messages.info(request,"Trip Added Successfully")
            return redirect('admin_dashboard')
        else:
            return redirect('add_trip')

def update_trip(request,id):
    if not request.session.get('email',None):
      return redirect('admin_login')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    trip=Trip.objects.get(trip_number=id)
    if request.method=="GET":
        return render(request,"adminn/updatetrain.html",{"train":trip})
    else:
            trip_number=request.POST.get('trip_number',None)
            avaliable_seats=request.POST.get('avaliable_seats',None)
            trip_data= request.POST.get('trip_data',None)
            trip_time = request.POST.get('trip_time',None)
            error=[]
            if(len(trip_number)<=1):
                error.append(1)
                messages.warning(request,"Please enter valid train in 3 digts...")
            if(not len(error)):
                manager=request.session['email']
                manager=Admin.objects.get(email=manager)
                trip.train_number=trip_number
                trip.avaliable_seats=avaliable_seats
                trip.trip_date=trip_data
                trip.trip_time=trip_time
                trip.save()
                messages.info(request,"Train Data Updated Successfully")
                return redirect('/dashboard1')
            else:
                return redirect('update_trip'+trip.train_number,{"trip":trip})

def viewprofile(request):
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('viewprofile_')
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
      email=request.session.get('email',None)
      data=Admin.objects.get(email=email)
      return render(request,"adminn/profile.html",{"data":data})
    else:
      return redirect("admin_login")

def updateprofile(request):
    if not request.session.get('email',None):
      return redirect('admin_login')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('customer_dashboard') 
    email=request.session.get('email',False)
    admin=Admin.objects.get(email=email)
    if request.method=="GET":
        return render(request,"adminn/Update.html",{"admin":admin})
    else:
            phone=request.POST.get('phone',False)
            date=request.POST.get('dateofbearth',False)
            password=request.POST.get('createpassword',False)
            repeat= request.POST.get('repeatpassword',False)
            error=[]
            if(len(password)<=1):
                error.append(1)
                messages.warning(request,"pass word field is empty")
            if(password!=repeat):
                error.append(1)
                messages.warning(request,"Invalid with Repeat password field")
            if(not len(error)):
                admin.phone=phone
                admin.birthday=date
                admin.password=password
                admin.save()
                messages.info(request,"Profile data Updated Successfully")
                return redirect('viewprofile')
            else:
                return redirect('viewprofile'+admin.id,{"admin":admin})
# Create your views here.
