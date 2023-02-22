from django.shortcuts import render, redirect
from .models import Personal 
from django.contrib import messages
from django.contrib.auth import authenticate
from sometut.views import HomePage

def signup(request):
    if request.method == "POST":
        if request.POST.get('user_id') and request.POST.get('user_name') and request.POST.get('age') and request.POST.get('Password'):
            saverec = Personal()
            saverec.user_id = request.POST.get('user_id')
            saverec.user_name = request.POST.get('user_name')
            saverec.age = request.POST.get('age')
            saverec.Password = request.POST.get('Password')
            
            allval=Personal.objects.all()
            
            for i in allval:
                if i.user_id == request.POST.get('user_id'):
                    messages.warning(request,'Please have a uniqe User ID...')
                    return render(request,'signup.html', )
                
        saverec.save()
        messages.success(request,'Welcome ' + saverec.user_name + ' in our service')
    
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        Password = request.POST.get('Password')
        
        user = authenticate(request, user_id=user_id, Password=Password)
        
        if user is not None:
            return redirect('HomePage')
        else:
            messages.info(request, 'Please enter valid passoword or User ID....')
            
    context = {}
    return render(request, 'login.html', context)
# Create your views here.
