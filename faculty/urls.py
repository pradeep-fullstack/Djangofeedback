from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login1',views.login1,name='login1'),
    path('reg',views.reg,name='reg'),
    path('reg1',views.reg1,name='reg1'),
    path('dashboard1',views.dashboard1,name='dashboard1'),
    path('logout1',views.logout1,name='logout1'),
    path('loginfct',views.loginfct,name='loginfct')
    
    ]