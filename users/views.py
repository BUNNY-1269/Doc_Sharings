from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


from .models import profile
from django.contrib.auth.models import User
from django.contrib import auth


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
        print(username)
    
        email=request.POST.get('newemail')
        
        password1=request.POST.get('pass1')
        print(password1)
        password2=request.POST.get('pass2')
        if password1 == password2:
           if User.objects.filter(username=username).exists():
              messages.info(request,'username taken')
              return render(request,'users/register.html')
           elif User.objects.filter(email=email).exists():
              messages.info(request,'Email Taken')
              return render(request,'users/register.html')
           else:
              user=User.objects.create_user(username=username,email=email,password=password1)
              user.save()
              return redirect('login')
        else:
            messages.info(request,'Password is not Matching')
            return render(request,'users/register.html')
    else:
      return render(request, 'users/register.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
@login_required
def profiles(request):
    if request.method == 'POST':
        my_dict = request.POST
        use=get_object_or_404(User,id=request.user.id) 
        print(my_dict['pict'])
        p1 = profile.objects.create(profilename=my_dict['profilename'], DOB=my_dict['DOB'], college=my_dict['college'],owner=use,image=my_dict['pict'])
        p1.save()
        return render(request, 'users/home.html')

    else:
        return render(request, 'users/profile.html')
def profileupdate(request):
    if request.method == 'POST':
        my_dict = request.POST
        use=get_object_or_404(User,id=request.user.id)



        p1 = profile.objects.get(owner=use)
        DO=p1.DOB
        college=p1.college

        p1.delete()
        p1=profile(profilename=my_dict['profilename'], DOB=DO, college=college,image=my_dict['pict'],owner=use)

        p1.save()
        return render(request, 'users/home.html')

    else:
        return render(request, 'users/profileupdate.html')

def createdprofile(request):

    use = get_object_or_404(User, id=request.user.id)
    p1=profile.objects.get(owner=use) 
    print(p1)
    return render(request,'users/createdprofile.html',{'p1':p1})
