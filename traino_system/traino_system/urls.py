"""traino_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import views
from adminn import views as mm
from customer import views as cus
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('booking.urls')),
    path('customer/',include('login.urls')),
    path('adminn/',include('login.urls')),
    path('logout/',views.logout,name='logout'),
    path('newtrain/',mm.add_train,name="add_train"),
    path('dashboard/',cus.dashboard,name="customer_dashboard"),
    path('newtrip/',mm.add_trip,name="add_trip"),
    path('updatetrip/<int:trip_number>/',mm.update_trip,name="update_trip"),
    path('profile_user/',cus.viewprofile,name='viewprofile_'),
    path('update_user/',cus.updateprofile,name='updateprofile_'),
    path('dashboard1/',mm.admin_dashboard,name="admin_dashboard"),
    path('updatetrain/<int:train_number>/',mm.update_train,name="update_train"),
    path('update_admin/',mm.updateprofile,name='updateprofile'),
    path('profile_admin/',mm.viewprofile,name='viewprofile'),

]