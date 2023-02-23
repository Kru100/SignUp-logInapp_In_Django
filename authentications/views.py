from django.shortcuts import render, redirect
from .models import Personal 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from sometut.views import HomePage
from django.contrib.auth.hashers import make_password, check_password

def signup(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        age = request.POST['age']
        password = request.POST['Password']
        hashed_password = make_password(password)
        personal = Personal(user_id=user_id, user_name=user_name, age=age, password=hashed_password)
        personal.save()
        messages.success(request, 'You have successfully registered.')
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['Password']
        try:
            personal = Personal.objects.get(user_id=user_id)
            #print(personal.password)
        except Personal.DoesNotExist:
            personal = None
        
        # is_cor
        # if is_correct is True:
        #     print('TRUE')
        # else:
        #     print('FALSE')
        if personal is not None and personal.password is not None and check_password(password, personal.password) is True:
            # print(personal.password)
            # user = authenticate(request, user_id=user_id, password=password, model=Personal)
            # print(user)
            # if user is not None:
                # login(request, user)
            return redirect('HomePage')
        error_msg = 'Invalid user ID or password. Please try again.'
        messages.error(request, error_msg)
        return redirect('login')
    else:
        return render(request, 'login.html')
            # allval=Personal.objects.all()
            # flag=True
            # for i in allval:
            #     if i.user_id == user_id and i.password == Password:
            #         flag = False
            #         break
            
            # print(flag)
            # if flag == False:
            #     #messages.info(request,'Please enter valid password or user ID') 
            #     return redirect('HomePage')
                       
    # context = {}
    # return render(request, 'login.html', context)
# Create your views here.
