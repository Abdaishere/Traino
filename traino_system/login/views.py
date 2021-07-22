from django.http.response import HttpResponse
from adminn.models import Admin
from django.contrib.messages.api import add_message
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from customer.models import Customer
#mesages.info(request,'mail taken')
def login(request):
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('email',None) and request.session.get('type',None)=='manager':
        return redirect('admin_dashboard')
    if request.method=="POST":
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        if Customer.objects.filter(email=email):
            user=Customer.objects.filter(email=email)[0]
            password_hash=user.password
            res=check_password(password,password_hash)
            if res==1:
                request.session['email'] = email
                request.session['type'] = 'customer'
                return render(request,'booking/home.html',{})
            else:
                messages.warning(request,"Username or password is incorrect")
                redirect('user_login')
        elif Admin.objects.filter(email=email):
            user=Admin.objects.filter(email=email)[0]
            password_hash=user.password
            res=check_password(password,password_hash)
            if res==1:
                request.session['email'] = email
                request.session['type'] = 'admin'
                return render(request,'booking/home.html',{})
            else:
                messages.warning(request,"Username or password is incorrect")
                redirect('admin_login')
        else:
            messages.warning(request,"No, Account exist for the given Username")
            redirect('home')
    else:
        redirect('user_login')
    return render(request,'login/login.html',{})
def user_register(request):
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        return redirect('admin_dashboard')
    if request.method=="POST":
        email=request.POST.get('email')
        email=request.POST.get('email')
        if Customer.objects.filter(email=email):
           messages.warning(request,"Account already exist, please Login to continue")
        else:
            first_name= request.POST.get('first_name',False)
            lastname=request.POST.get('last_name',False)
            typee= request.POST.get('gender',False)
            email=request.POST.get('email',False)
            if  Admin.objects.filter(email=email):
                messages.warning(request,"Account already exist, please Login to continue")
            else:
                phone_no=request.POST.get('phone',False)
                date = request.POST.get('dateofbearth',False)
                password=request.POST.get('password',False)
                repeat= request.POST.get('repeat',False)
                #profile_pic=request.FILES.get('profile_pic',None)
                if password!=repeat:
                    messages.warning(request,"Password not equal reapted one")
                    redirect('user_signup')
                password_hash = make_password(password)
                r_manager=Admin(first_name=first_name,last_name=lastname,email=email,phone=phone_no,birthday=date,password=password_hash,access_code=access)
                r_manager.save()
                messages.info(request,"Account Created Successfully, Please login to continue")
                redirect('user_login')
    else:
        redirect('user_signup')
    return render(request,"login/admin_register.html")
def admin_register(request):
    if request.session.get('email',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('email',None) and request.session.get('type',None)=='admin':
        return redirect('admin_dashboard')
    if request.method=="POST":
        first_name= request.POST.get('first_name',False)
        lastname=request.POST.get('last_name',False)
        typee= request.POST.get('gender',False)
        email=request.POST.get('email',False)
        if  Admin.objects.filter(email=email):
           messages.warning(request,"Account already exist, please Login to continue")
        else:
            phone_no=request.POST.get('phone',False)
            date = request.POST.get('dateofbearth',False)
            password=request.POST.get('password',False)
            repeat= request.POST.get('repeat',False)
            access = request.POST.get('accesscode',False)
            #profile_pic=request.FILES.get('profile_pic',None)
            if password!=repeat:
                messages.warning(request,"Password not equal reapted one")
                redirect('admin_signup')
            if access!=1234:
                messages.warning(request,"Check your Acess code")
                redirect('admin_signup')
            password_hash = make_password(password)
            r_manager=Admin(first_name=first_name,last_name=lastname,email=email,phone=phone_no,birthday=date,password=password_hash,access_code=access)
            r_manager.save()
            messages.info(request,"Account Created Successfully, Please login to continue")
            redirect('user_login')
    else:
        redirect('admin_signup')
    return render(request,"login/admin_register.html")
def logout(request):
    if request.session.get('email', None):
        del request.session['email']
        del request.session['type']
        return render(request,"booking/home.html",{})
    else:
        return render(request,"login/login.html",{})
