from django.urls import path
from .views import *

urlpatterns=[
    path('index/', indexrender, name="index"),
    path('login/', login, name="login"),
    path('login1/' ,login1,name="login1"),
    path('register/',Register,name="register"),
    path('sign/',signup1,name='signup1'),
    path('home/',homerender,name="home"),
    path('logout/',logout,name='logout'),
    path('index2',index2,name='index2'),
    path('contactus/',contactusrender,name="contactus"),
]
