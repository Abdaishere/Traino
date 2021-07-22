from django.urls import path,include
from . import views
urlpatterns=[
    path('login',views.login,name='user_login'),
    path('login1',views.login,name='admin_login'),
    path('register',views.user_register,name='user_signup'),
    path('register1',views.admin_register,name='admin_signup'),
]