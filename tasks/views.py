from django.shortcuts import render, HttpResponse, redirect
import smtplib
from django.contrib.auth import authenticate, login, logout
from .models import Detail
from .models import Contact
from .models import Book
from django.contrib.auth.models import User
from django.contrib import messages
from tkinter import ttk
from tkinter import Tk
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import FormView
import time
from .forms import *
import os
import requests
from django.core.serializers import serialize
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        users = request.POST['username']
        email = request.POST['email']
        if request.POST['password'] == request.POST['confirm_password'] and len(request.POST['password']) > 8:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already exist, Please Try Again'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=users, password=request.POST['password'])
                user.first_name = first_name
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
            return render(request, 'login.html', {'error' : "Do not match login detail"})
    else:
        return render(request, 'login.html')

def shivam(request, data, id): # dyanamic urls test
    return HttpResponse('<h1>This is Shivam Page {} and {}</h1>'.format(data, id))

def st(request):# dynamic urls test
    if(request.method == 'GET' and 'id' in request.GET and 'data' in request.GET):
        return HttpResponse('<h1>This is Shivam Page data is {} and id is {}</h1>'.format(request.GET.get('data'),request.GET.get('id')))
    else:
        return HttpResponse('This is our page')

def tata(request, pk=None):
    if pk is None:
        det = Book.objects.all()
    else:
        det = Book.objects.filter(pk=pk)
    ta = serialize('json', det)
    return HttpResponse(ta, content_type='application/json')

class tempform(FormView):
    template_name = 'formses.html'
    form_class = contact_form
    success_url = '/'

class classes(TemplateView):
    template_name = 'cbv.html'

def contactform(request):
    if request.method == 'POST':
        form = contact_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = contact_form()
    return render(request, 'formses.html', {'form': form})
