from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('show/',views.show_booking,name='show_booking'),
    path('book/<str:id>',views.book, name='book'),
    path('visa/',views.visa,name='visa'),
    path('fawary/',views.fawaryy,name='fawaryy'),
    path('visa_data/',views.inside_visa,name="inside_visa"),
    path('inside_fawary/',views.inside_fawary,name="inside_fawary"),
    path('cancel-trip/<str:id>',views.cancel_trip,name='cancel-trip'),
    path('confirm-now',views.book_confirm,name="book_confirm"),
]
