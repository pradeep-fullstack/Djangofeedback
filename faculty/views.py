from django.shortcuts import render,redirect
from.models import Regfact
def index(request):
	return render(request,'faculty/index.html')
def login1(request):
	return render(request,'faculty/login.html')
def reg(request):
	return render(request,'faculty/reg.html')
def reg1(request):
    name=request.POST['t1']
    email=request.POST['t2']
    pas=request.POST['t3']
    num=request.POST['t4']
    obj=Regfact(name=name,email=email,pas=pas,num=num)
    obj.save()
    return render(request,"faculty/reg.html",{'res':"data submited successfully"})
def loginfct(request):
    email=request.POST['email']
    pas=request.POST['password']
    s=Regfact.objects.filter(email=email,pas=pas)
    if(s.count()==1):
        request.session['uid']=email
        return redirect('dashboard1')
    else:
        return redirect('login1')
def dashboard1(request): 
   if(request.session.has_key('uid')): 
    dt=Regfact.objects.get(email=request.session['uid'])
    return render(request,'faculty/dashboard.html',{'data':dt})
def logout1(request):
    del request.session['uid']
    return redirect("login1")