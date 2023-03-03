from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login 
from .models import *



# Create your views here.

def index(request):
    return HttpResponse('Hey buddy, you have reached index page.')


def login1(request):
    
    if request.method == 'GET':
        context = {
            'msg1': 'This is login page'
        }
        return render(request, 'login1.html', context)
    
    # if request.method == 'POST':
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     user = authenticate(fname=fname,lname = lname, email = email)
    #     print()
    #     if user is not None:
    #         login(request, user)
    #         return redirect('dashboard')
    
    else:
        
        email = request.POST['email']
        users = signup_db.objects.all()
        user_email = []
        for user in users:
            user_email.append(user.email)
        # print(user_email)

        if email in user_email:
            context = {
                'msg2':'login successful',
                'msg3': email
            }
            request.session['value1'] = email # publishing value1
            return redirect('dashboard')
        else:
            return redirect('sign_up')    
    # else:
    #     return render(request, 'login1.html', {'msg1': 'This is login page'})

def sign_up(request):
    
    if request.method == 'GET':
        context = {
            'msg1': 'This is sign_up page for new user account creation'
        }
        return render(request, 'sign_up.html', context)

    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        person, created = signup_db.objects.get_or_create(fname=fname, lname=lname, email=email)
        if created:
            # messages.info(request, 'Data inserted and account created successfully')
            # return render(request, 'sign_up.html', {'msg2':'use your sign_up credentials for login'})
            # audio_db1.objects.create(email = email, signup_db_user = person) # to be used when paralley data needs to be inserted inside audio_db1
            return render(request, 'login1.html', {'msg2':'Data inserted and account created successfully'})
        
        else:
            # messages.info(request, 'User already exists')
            # return render(request, 'sign_up.html', {'msg2':'use your sign_up credentials for login'})
            request.session['value2'] = 'User already exists'
            return redirect('login1')


def logout(request):
    return redirect('login1')


# @login_required(login_url='login1')
def dashboard(request):
    value1 = request.session.get('value1')  # value1 is coming from login1
    msg4 = audio_db1.objects.filter(email= value1)  # fetching/get from audio_db1
    # msg5 = request.session.get('msg5')  # coming from record_audio, to be used if any message from record_audio is to be shown in dashboard
    context = {
        'msg2' : 'welcome to dashboard',
        'msg3' : value1,
        'msg4' : msg4,
        # 'msg5': msg5,
    }
    return render(request, 'dashboard.html', context)
