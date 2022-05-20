from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def form(request):
    if request.method =='POST':
     password1=request.POST['password1']
     password2=request.POST['password2']
     username=request.POST['username']
     first_name=request.POST['first_name']
     last_name=request.POST['last_name']
     email=request.POST['email']
     if password1==password2:
        if User.objects.filter(username=username).exists():
             messages.info(request,'username exists')
             return redirect('/')
        elif User.objects.filter(email=email).exists():
             messages.info(request,'email exists')
             return redirect('/')
        else:
             user=User.objects.create_user(password=password1,username=username,first_name=first_name,last_name=last_name,email=email)
             user.save();
             messages.info(request,'great')
             return redirect('/')
     else:
        messages.info(request,'not great')
        return redirect('/')
    else:
        return render(request,'form.html')

def login(request):
    if request.method =='POST':
        password=request.POST['password']
        username=request.POST['username']
        user=auth.authenticate(password=password,username=username)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'login again')
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('/')
    else:
        messages.info(request,'successful')
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


