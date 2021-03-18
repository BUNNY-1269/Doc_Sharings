from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .models import File
from .forms import DocumentForm

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
def uploadfile(request):
    if request.method=='POST':
      form1=request.POST.get('file')
      DocumentForm(files=form1)
      form=DocumentForm(request.POST,request.FILES)
      if form.is_valid():
        for field in request.FILES.keys():
            for formfile in request.FILES.getlist(field):
                f = File(file=formfile, user=request.user)
                f.name = f.filename()
                f.save()
        return redirect('My_Files')
      else:
        return redirect('My_Files')
def ousersfile(request,user):
    print(user)
    ruser=User.objects.get(username=user)
    all_files = File.objects.filter(user=ruser)
    context = {'all_files': all_files, 'u': ruser}
    return render(request, 'filesharing/ousersfile.html', context)    
def delete(request,pk):
    user = request.user
    all_files = File.objects.filter(user=user)
    file=all_files.filter(pk=pk)
    file.delete()

    return redirect('My_Files')
