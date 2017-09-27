# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import bcrypt
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Create your views here.
def home(request):
    return render(request, 'logreg/home.html')
a

def show(request):
    context = {
        "form": Sign_in_forms,
    }
    return render(request, 'logreg/sign_in.html', context)

def show_reg(request):
    context = {
        "formy": Register_forms,
    }
    return render(request, 'logreg/register.html', context)

def sign_in(request):
    errors = Users.objects.login_valid(request.POST)
    em = request.POST['email']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/sign_in')
    request.session['log_id'] = Users.objects.get(email=em).id
    request.session['fname'] = Users.objects.get(email=em).fname
    request.session['access'] = Users.objects.get(email=em).access
    if request.session['access']=="Admin":
        return redirect('/dashboard/admin')
    request.session['path'] = "Log path"
    return redirect('/dashboard')



def register(request):
    errors = Users.objects.users_valid(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())

        Users.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], pw=hash1)
        request.session['path']= "Reg path"
        request.session['fname'] = request.POST['fname']
        em = request.POST['email']
        request.session['access'] = Users.objects.get(email=em).access
        abc = Users.objects.get(email=em).id
        request.session['log_id'] = abc

    return redirect('/dashboard')