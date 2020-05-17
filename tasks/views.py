from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Detail
import datetime
from django.utils import timezone
import requests
import pytz
import json
def signup(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        last_name = request.POST['last_name']
        users = request.POST['username']
        email = request.POST['email']
        if request.POST['password'] == request.POST['confirm_password'] and len(request.POST['password']) > 8:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already exist, Please Try Again'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=users, password=request.POST['password'])
                user.f_name = f_name
                user.last_name = last_name
                user.email = email
                user.save()
                messages.success(request, "Your Account created Successfully")
                return redirect('/signup')
        else:
            return render(request, 'signup.html', {'errors': 'Password not Match and your password length should be 8 character , Please Try Again'})
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        psw = request.POST['psw']
        user = authenticate(username=uname, password=psw)
        if user is not None:
            login(request, user)
            return render(request, 'see.html')
        else:
            return render(request, 'login.html', {'error': "Do not match login detail"})
    else:
        return render(request, 'login.html')

def see(request):
    if request.method == 'POST':
        name = request.POST['name']
        tz = request.POST['tz']
        emails = request.POST['emails']
        text = request.POST['text']
        start_datetime = timezone.now()
        end_datetime = datetime.datetime.now()
        inf = Detail(name=name, tz=tz, emails=emails, text=text, start_datetime=start_datetime, end_datetime=end_datetime)
        members = {
            'Name': name,
            'Tz': tz,
            'Emails': emails,
            'Text': text,
            'Activity_Periods':
                {'start_time': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                 'end_time': end_datetime.strftime('%Y-%m-%dT%H:%M:%S')},
        }
        if Detail.objects.filter(emails__exact=emails):
            members['Activity_Periods'] = {'start_time': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),'end_time': end_datetime.strftime('%Y-%m-%dT%H:%M:%S')}
            g = open('s.json', 'w')
            g.write(json.dumps(members))
            g.close()
        elif name != 'default':
            inf.save()
            s = json.dumps(members)
            f = open('s.json', 'w')
            f.write(json.dumps(s))
            f.close()
        else:
            return HttpResponse("This email id is already registered")
    return render(request, 'see.html')