from django.contrib.auth.models import User
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
# Create your views here.
from .models import File,Folder
from .forms import DocumentForm
from django.views.generic.edit import FormView,DeleteView,UpdateView
def index(request):
    ruser = User.objects.get(username=user)
    all_files = File.objects.filter(user=ruser)
    all_folders = Folder.objects.filter(user=ruser)
    top_folder = Folder.objects.filter(linkedfolder__isnull=True)
    top_file = File.objects.filter(folder__isnull=True)
    context = {'all_files': top_files, 'u': ruser, 'all_folders': top_folders}

    return render(request, 'filesharing/index.html', context)

def detail(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    # Try folder_set.all() when model is 'folder' instead of 'Folder'
    temp = folder
    parent_list = []
    parent_list.append(temp)
    while temp.linkedfolder:
        parent = temp.linkedfolder
        parent_list.append(parent)
        temp = parent
    active_folder = parent_list[0]
    parent_list.reverse()
    context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id,'parent_list':parent_list,'active_folder':active_folder}
    return render(request,'filesharing/details.html',context)

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
def uploadfile(request):  #changed
    if request.method=='POST':

            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():
                for field in request.FILES.keys():
                    for formfile in request.FILES.getlist(field):
                        f = File(file=formfile, user=request.user)
                        f.name = f.filename()
                        f.save()
                return redirect('filesharing:index')
            else:
                return render(request, 'filesharing/file_form.html', {'form': form})
    else:
            form = DocumentForm(None)
            return render(request, 'filesharing/file_form.html', {'form': form})
def uploadlinkedfile(request,pk):   #added
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    f = File(file=formfile, user=request.user)
                    f.name = f.filename()
                    f.folder=Folder.objects.get(pk=pk)
                    f.save()
            return redirect('filesharing:index')
        else:
            return render(request, 'filesharing/file_form.html', {'form': form})
    else:
        form = DocumentForm(None)
        return render(request, 'filesharing/file_form.html', {'form': form})
class FileDelete(DeleteView):
    model = File

    def get_success_url(self):
        f = File.objects.get(pk = self.kwargs['pk'])
        folder = f.folder
        if not folder:
            return reverse_lazy('fileshare:index')
        else:
            return reverse_lazy('fileshare:detail',kwargs={'folder_id': folder.pk})

    def get(self, *args, **kwargs):
            return self.post(*args, **kwargs)


def ousersfile(request,user):
    ruser=User.objects.get(username=user)
    all_files = File.objects.filter(user=ruser)
    all_folders=Folder.objects.filter(user=ruser)
    top_folder=Folder.objects.filter(linkedfolder__isnull=True)
    top_file=File.objects.filter(folder__isnull=True)
    context = {'all_files':top_file, 'u': ruser,'all_folders':top_folder}
    return render(request, 'filesharing/ousersfile.html', context)    
# def delete(request,pk):
#     user = request.user
#     all_files = File.objects.filter(user=user)
#     file=all_files.filter(pk=pk)
#     file.delete()
#
#     return redirect('My_Files')

def makeprivate(request,pk):
    user = request.user
    all_files = File.objects.filter(user=user)
    gfile = all_files.get(pk=pk)
    gfile.isprivate = True
    gfile.save(update_fields = ["isprivate"])
    all_files = File.objects.filter(user=user)
    context = {'all_files': all_files, 'u': user}

    return redirect('My_Files')



def makepublic(request,pk):
    user = request.user
    all_files = File.objects.filter(user=user)
    gfile = all_files.get(pk=pk)
    gfile.isprivate = False
    gfile.save(update_fields=["isprivate"])
    all_files = File.objects.filter(user=user)
    context = {'all_files': all_files, 'u': user}
    return redirect('My_Files')







