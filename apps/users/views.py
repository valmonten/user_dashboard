# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def new(request):
    return render(request, 'users/index.html')

def show(request, name):
    #Show messages from database
    #query db and send it through with context
    d = Users.objects.get(id=name)
    e = Messages_Posted.objects.filter(user_to = d)
    f = Comments_Posted.objects.all()
    # import pdb; pdb.set_trace()
    context = {
        "user":d,
        "form1":Message_Form,
        "msgs":e,
        "form2":Comment_Form,
        "cmts":f,
    }



    return render(request, 'users/show.html',context)

def post(request):
    # creating(request.POST)
    at = request.POST['return_id']
    a = '/users/show/'+str(at)
    msg = request.POST['msg']
    login = request.session['log_id']
    userf = Users.objects.get(id=login)
    tuser = Users.objects.get(id=at)
    Messages_Posted.objects.create(msg=msg, user_from=userf, user_to=tuser)
    return redirect(a)

def comment(request):
    at = request.POST['return_id1']
    b = request.POST
    
    a = '/users/show/'+str(at)
    comment = request.POST['cmt']
    login = request.session['log_id']
    userf = Users.objects.get(id=login)
    msg_id = request.POST['message_on']
    on = Messages_Posted.objects.get(id=msg_id)
    Comments_Posted.objects.create(cmt=comment, on_msg=on, user_from=userf)
    return redirect(a)

def admin_edit(request, idd):
    
    c = Users.objects.get(id=idd)

    context = {
        "user": c,
        "form":Edit,
        "pwform":Change_Pw,
    }
    return render(request, 'users/admin_edit.html', context)

def editting(request):
# Pulls all the errors from models
    errors = Users.objects.edit_user(request.POST)
    # Checks if there are errors to display then redirects if there are
    ident = request.POST['idt']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+str(ident))
        # Else saves the edited form and resets session data
    else:

        me = request.POST
        a = Users.objects.get(id=me['idt'])
        a.fname=me['fname']
        a.lname=me['lname']
        a.email=me['email']
        a.access=me['access']
        a.save()
        if ident == request.session['id']:
            request.session['fname'] = request.POST['fname']
            em = request.POST['email']
            request.session['email'] = em
            request.session['access'] = Users.objects.get(email=em).access

    if request.session['access'] == "Admin":
        return redirect('/dashboard/admin/')
    else:
        return redirect('/dashboard/')

def pwc(request):
    errors = Users.objects.edit_pw(request.POST)
    ident = request.POST['idt']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+str(ident))

    hashed = bcrypt.hashpw(request.POST['new_pw'].encode(), bcrypt.gensalt())
    t = Users.objects.get(id=ident)
    t.pw = hashed
    t.save()

    if request.session['access'] == "Admin":
        return redirect('/dashboard/admin/')
    else:
        return redirect('/dashboard/')

def off(request):
    request.session.clear()
    return redirect('/')

def edit(request):
    context = {
        'form':Change_Pw
    }
    return render(request, 'users/edit.html', context)
def desc(request):
    a = request.session['log_id']
    b = Users.objects.get(id=a)
    b.desc = request.POST['desc']
    b.save()
    return redirect('/dashboard')