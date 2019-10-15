from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('token/',views.token,name='token'),
     path('staff/',views.staff,name='staff'),
     path('nextone/',views.nextone,name='nextone'),
   
]