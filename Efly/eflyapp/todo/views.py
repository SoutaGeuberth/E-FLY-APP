from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request,'todo/home.html')

def register(request):
    if request.method == 'POST':
        form = CreateUsuarioForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = CreateUsuarioForm()

    context = {'form': form}     
    return render(request, 'todo/userRegister.html', context)

@login_required
def ChangePassword(request):

    if request.method == 'POST':
        form = ChangePasswordForm(request.user,request.POST)        
        if form.is_valid(): 

            user=form.save()
            update_session_auth_hash(request,user)
            return redirect('home')
    else:
        form = ChangePasswordForm(request.user)

    context = {'form': form}    
    return render(request, 'todo/changePassword.html', context)

@login_required
def Edit(request,DNI):
    perfil=get_object_or_404(CustomUser,DNI=DNI)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=perfil)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = EditForm(instance=perfil)

    context = {'form': form}     
    return render(request, 'todo/Edit.html', context)

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def eliminateUser(request,DNI):
    
    user = CustomUser.objects.get(DNI=DNI)
    user.delete()
    return redirect('home')

