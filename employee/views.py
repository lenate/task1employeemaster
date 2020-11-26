from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *



def home(request):
    return render(request,"empfirst.html")

def about(request):
    return render(request,"about.html")

def regstr(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        uname = request.POST.get('uname')
        
        
        password=request.POST.get('pswd1')
        password2=request.POST.get('pswd2')
        
        utyp='user'
       
        Users.objects.create_user(first_name=fname,last_name=lname,email=email,password=password2,username=uname,usertype=utyp)
        return redirect(logins)
    else:
        return render(request,'register.html',{'success':'Registered Successfully!'})

def logins(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=uname, password=pswd)
        if user is not None and user.is_staff == 1:
            return redirect(home)
        elif user is not None and user.usertype == 'user':
            login(request,user)
            return redirect(home)
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logouts(request):
    logout(request)
    return redirect(logins)

def add(request):
    
   
    if request.method=="GET":
         return render(request,'empadd.html')
    else:
        prop=Employees()
        prop.EmployeeName=request.POST.get('ename')
        prop.Address=request.POST.get('address')
        prop.Phone=request.POST.get('phone')
        prop.Email=request.POST.get('email')
        
        prop.Image=request.FILES['img']
       
        
        prop.save()
        return redirect(vemp)

def vemp(request):
    vemp=Employees.objects.all()
    return render(request,'emppview.html',{'data': vemp})

def delemp(request, em_id):
    demp = Employees.objects.get(id=em_id)
    demp.delete()
    
    return redirect(vemp)

def editemp(request, em_id):
    if request.method == 'GET':
        upemp = Employees.objects.get(id=em_id)
        return render(request, 'empupdate.html', {'data':upemp})
    else:
        updata = Employees.objects.get(id=em_id)
       
        updata.EmployeeName = request.POST.get('ename')
        
        updata.Address = request.POST.get('address')
        updata.Phone = request.POST.get('phone')
        updata.Email = request.POST.get('email')
            
        updata.save()
        return redirect(vemp)    