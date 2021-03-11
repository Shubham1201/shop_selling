from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
import datetime

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
        shopnamevar = request.POST.get('shopn')
        logged_user = User.objects.get(username=request.user.username)
        amount = float(amount)
        
        godata = customers.objects.create(shopkipper=logged_user, shopname=merchant.objects.get(shopname=shopnamevar), customername=customer, selldetail=sellingdetail, dates=datetime.date.today(), selling=amount)
        godata.save()
        return redirect('/')
    else:
        logged_user = User.objects.get(username=request.user.username)
        mer_user = merchant.objects.filter(shopkipper=logged_user).all()
        return render(request, 'addentry.html', {'merchant': mer_user})

def History(request):
    logged_user = User.objects.get(username=request.user.username)
    mer_user = merchant.objects.filter(shopkipper=logged_user).all()
    dataset = customers.objects.filter(shopkipper=logged_user).all()
    return render(request, 'history.html', {'dataset': dataset, 'merchant': mer_user})