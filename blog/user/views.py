from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileModelForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def signUp(request):
    form= RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def signIn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def signOut(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profilePage(request):
    
    return render(request, 'profile.html')

@login_required(login_url='login')
def profileEdit(request, pk):
    edit_inst = Profile.objects.get(id = pk)
    editForm = ProfileModelForm()
    if request.method == 'POST':
        editForm= ProfileModelForm(request.POST, request.FILES, instance=edit_inst)
        if editForm.is_valid():
            editForm.save()
            return redirect('profile')
    else:
        editForm = ProfileModelForm(instance=edit_inst)
    context = {
        'edit_inst' : edit_inst,
        'editForm' : editForm
    }
    return render(request, 'profile-edit.html', context)