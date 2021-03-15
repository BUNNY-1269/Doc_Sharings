from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .models import File


def home1(request):
    return render(request,'filesharing/home1.html')

def allusers(request):
    all_users = User.objects.all();
    current_user = request.user
    return render(request, 'filesharing/users.html', {'all_users': all_users, 'current_user': current_user})
def My_Files(request):
    user = request.user
    all_files = File.objects.filter(user=user)
    context = { 'all_files':all_files,'u':user }
    return render(request, 'filesharing/MY_Files.html', context)