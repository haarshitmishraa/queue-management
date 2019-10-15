    
from django.shortcuts import render, redirect
from django.http import HttpResponse
import sys
from .forms import queueForm
from . import script




def token(request):
    tokenNO = 1
    if request.method == 'POST':
        purpose=request.POST['select']
        phone = request.POST['phone']
        
        x,y = script.calll()
       
        context = {'token': x,'phone':phone,'purpose': purpose,'after':y}
        
    return render(request,'queue_app/token_page.html',context)


def home(request):
    if request.method == 'POST':
        form = queueForm(request.POST)

        if form.is_valid():
            return redirect('token')

        
    else:
        form = queueForm()

    context = {'form':form}

    return render(request,'queue_app/index.html', context)



    return render(request,'queue_app/index.html')


def staff(request):    
    x = script.count()
    context = {'next':x}
    return render(request,'queue_app/staff.html',context)


def nextone(request):
    x = script.next()
    context = {'next': x}
    
    return render(request,'queue_app/staff.html',context)


