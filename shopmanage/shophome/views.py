from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.
def homeapp(request):
    return render(request, 'index.html')

def signUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            

    else:
        return render(request, 'signup.html')
    
    return redirect('login')
    

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    else: 
        return render(request, 'login.html')
    
def logOut(request):
    auth.logout(request)
    return redirect('/')

def addShop(request):
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        
        godata = merchant.objects.create(shopkipper=User.objects.get(id=request.user.id), shopname=shopname)
        godata.save()
        return redirect('/')

    else:
        return render(request, 'addshop.html')

def addEntry(request):
    if request.method == "POST":
        customer = request.POST.get('customer')
        sellingdetail = request.POST.get('sellingdetail')
        amount = request.POST.get('amount')

        godata = customers.objects.create(shopkipper=User.objects.get(id=request.user.id), shopname=merchant.objects.get(shopname), customername=customer, selldetail=sellingdetail, selling=amount)
        godata.save()
        return redirect('/')
    else:
        return render(request, 'addentry.html', {'merchant': merchant.objects.all()})