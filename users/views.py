from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
from .forms import UserUpdateForm
from .models import Profile


def home(request):
    return render(request,'users/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home1')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
      return render(request, 'users/login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        if password1 == password2:
           if User.objects.filter(username=username).exists():
              messages.info(request,'username taken')
              return render(request,'users/register.html')
           elif User.objects.filter(email=email).exists():
              messages.info(request,'Email Taken')
              return render(request,'users/register.html')
           else:
              user=User.objects.create_user(username=username,email=email,password=password1)
              user.save();
              return render(request,'users/login.html')
        else:
            messages.info(request,'Password is not Matching')
            return render(request,'users/register.html')
    else:
      return render(request, 'users/register.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'users/profile.html', context)
