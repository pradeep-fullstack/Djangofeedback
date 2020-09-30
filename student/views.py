
from django.shortcuts import render,redirect
from.models import Register
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('ckey', 'karisma ho gaya')  
    return response  

def getcookie(request):  
    a  = request.COOKIES['ckey']  
    return HttpResponse("value is "+  a)

def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs=FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'student/fileupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'student/fileupload.html')

def index(request):
    return render(request,"student/index.html")
def about(request):
    return render(request,"student/about.html")
def ShowReg(request):
    s=Register.objects.all()
    return render(request,"student/ShowReg.html",{'vis':s})
def registration(request):
    return render(request,"student/registration.html")
  
def registration1(request):  
    name=request.POST['t1']
    email=request.POST['t2']
    pas=request.POST['t3']
    num=request.POST['t4']
    obj=Register(name=name,email=email,pas=pas,num=num)
    obj.save()
    return render(request,"student/registration.html",{'res':"data submited successfully"})
def EditReg(request):
    sid=Register.objects.get(pk=request.GET["q"])
    return render(request,"student/EditReg.html",{'res':sid})
def EditRegData(request):
    n=request.POST['t1']
    e=request.POST['t2']
    p=request.POST['t3']
    num1=request.POST['t4']
    s=Register.objects.get(pk=request.POST["ids"])
    s.name=n
    s.email=e
    s.pas=p
    s.num=num1
    s.save()
    return redirect("ShowReg")
     
def DeleteReg(request):
	sid=Register.objects.get(pk=request.GET["q"])
	sid.delete()
	return redirect("ShowReg")
def login(request):
        return render(request,"student/login.html")
def loginstd(request):
    em=request.POST['email']
    pas=request.POST['password']
    s=Register.objects.filter(email=em,pas=pas)
    if(s.count()==1):
        request.session['sid']=em
        response = HttpResponse("Cookie Set")  
        response.set_cookie('ckey', "gagan") 
        return redirect("dashboard")
    else:
        return redirect("login")
def dashboard(request):
    if(request.session.has_key('sid')):
        dt=request.session['sid']
        return render(request,"student/dashboard.html",{'data':dt})
    else:
        return render(request,"student/login.html")
   
def logout(request):
    del request.session['sid']
    return redirect("login")