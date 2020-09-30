from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('loginstd',views.loginstd,name='loginstd'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('ShowReg',views.ShowReg,name='ShowReg'),
    path('registration1',views.registration1,name='registration1'),
    path('registration',views.registration,name='registration'),
    path('EditReg',views.EditReg,name='EditReg'),
    path('EditRegData',views.EditRegData,name='EditRegData'), 
    path('DeleteReg',views.DeleteReg,name='DeleteReg'),
    path('fileupload',views.fileupload,name="fileupload"),
    path('setcookie',views.setcookie,name='setcookie'),
    path('getcookie',views.getcookie,name='getcookie'),

   ]