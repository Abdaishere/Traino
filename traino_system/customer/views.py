from django.core.checks import messages
import booking
from customer.models import Customer
from django.shortcuts import render,redirect
from booking import models 

def dashboard(request):
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        return redirect('admin_dashboard')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
      email=request.session['email']
      data=Customer.objects.get(email=email)
      booking_data=booking.objects.filter(user_id=data).order_by('-id')
      return render(request,"customer/dashboard.html",{"data":booking_data})
    else:
      return redirect("user_login")
def viewprofile(request,id):
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        return redirect('admin_profile')
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
      email=request.session['email']
      data=Customer.objects.get(email=email)
      return render(request,"customer/profile.html",{"data":data})
    else:
      return redirect("user_login")

def updateprofile(request):
    if not request.session.get('email',None):
      return redirect('user_login')
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        return redirect('admin_dashboard') 
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    if request.method=="GET":
        return render(request,"customer/Update.html",{"customer":customer})
    else:
            phone=request.POST['phone']
            date=request.POST['dateofbearth']
            password=request.POST['createpassword']
            repeat= request.POST['repeatpassword']
            error=[]
            if(len(password)<=1):
                error.append(1)
                messages.warning(request,"pass word field is empty")
            if(password!=repeat):
                error.append(1)
                messages.warning(request,"Invalid with Repeat password field")
            if(not len(error)):
                customer.phone=phone
                customer.birthday=date
                customer.password=password
                customer.save()
                messages.info(request,"Profile data Updated Successfully")
                return redirect('/customer/profile_user/')
            else:
                return redirect('/customer/profile_user/'+customer.id,{"customer":customer})
# Create your views here.
