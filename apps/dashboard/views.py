# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..logreg.models import *



def dash(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)
def admin(request):
    if request.session['access']!="Admin":
        return redirect('/dashboard/')
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dashboard/admin.html', context)