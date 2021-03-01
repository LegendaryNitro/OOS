from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegister
from .decorator import unauthorized_user, allowed_users, admin_only
from .usersF import *

ff="usersF"
def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            theUser=form.save()
            theUsername=form.cleaned_data.get('username')

            group= Group.objects.get(name='customer')
            theUser.groups.add(group)

            messages.success(request, f'account created, you can login')
            return redirect('login')

    else:
        form= UserRegister()
       
    return render(request, f'{ff}/register.html', {'form':form })

@login_required()
@allowed_users(allowed_roles=['customer'])
def profile(request):
    return render(request, f'{ff}/view1.html')



def loginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')


        theUser=authenticate(request, username=username, password=password)

        if theUser is not None:

            login(request, theUser)
            return redirect(f'{ff}/view1.html')
        else:
            messages.info(request, 'username or Password doesn\'t match')

    context={

    }

    return render(request, f'{ff}/view1.html', context)


def logoutUser(request):
    logout(request)

    return redirect('login')
@login_required()
def home(request):
    return render(request,f'{ff}/view1.html')
