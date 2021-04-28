from django.contrib.auth.models import User
from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
from .models import File,Folder
from .forms import DocumentForm,FolderUploadForm,FolderForm
from django.views.generic.edit import FormView,DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# def detail(request,folder_id):
#      folder = get_object_or_404(Folder,pk=folder_id)
#      files = folder.file_set.all()
#      folders = folder.folder_set.all()
#      print('details')
#      # Try folder_set.all() when model is 'folder' instead of 'Folder'
#      temp = folder
#      parent_list = []
#      parent_list.append(temp)
#      while temp.linkedfolder:
#          parent = temp.linkedfolder
#          parent_list.append(parent)
#          temp = parent
#      active_folder = parent_list[0]
#      parent_list.reverse()
#      context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id,'parent_list':parent_list,'active_folder':active_folder}
#      return render(request,'filesharing/details.html',context)

def user_details(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    print('user_details')
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
    return render(request,'filesharing/user_linkedfiles.html',context)
# def othersdetails(request,folder_id):
#     folder = get_object_or_404(Folder,pk=folder_id)
#     files = folder.file_set.all()
#     folders = folder.folder_set.all()
#     print('user_details')
#     # Try folder_set.all() when model is 'folder' instead of 'Folder'
#     temp = folder
#     parent_list = []
#     parent_list.append(temp)
#     while temp.linkedfolder:
#         parent = temp.linkedfolder
#         parent_list.append(parent)
#         temp = parent
#     active_folder = parent_list[0]
#     parent_list.reverse()
#     context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id,'parent_list':parent_list,'active_folder':active_folder}
#     return render(request,'filesharing/details.html',context)

def insidefolders(request,folder_id):
     f=get_object_or_404(Folder,pk=folder_id)
     files=f.folder_set.all()
     folders=f.folder_set.all()
     temp=f
     parent_list=[]
     parent_list.append(temp)
     while temp.linkedfolder:
         parent=temp.linkedfolder
         parent_list.append(parent)
         temp=parent
     active_f=parent_list[0]
     parent_list.reverse()
     context = {'folder': f, 'folders': folders, 'files': files, 'folder_id': folder_id, 'parent_list': parent_list,
                'active_folder': active_f}
     return render(request, 'filesharing/details.html', context)


def home1(request):
    return render(request,'filesharing/home1.html')

def allusers(request):
    all_users = User.objects.all();
    current_user = request.user
    return render(request, 'filesharing/users.html', {'all_users': all_users, 'current_user': current_user})
def My_Files(request):
    user = request.user
    all_files = File.objects.filter(user=user)
    all_folders = Folder.objects.filter(user=user)
    top_folder = all_folders.filter(linkedfolder__isnull=True)
    top_file = all_files.filter(folder__isnull=True)
    context = {'all_files': top_file, 'all_folders': top_folder}

    return render(request, 'filesharing/MY_Files.html', context)
def uploadfile(request):  #changed
    if request.method =='POST':

            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():
                for field in request.FILES.keys():
                    for formfile in request.FILES.getlist(field):
                        f = File(file=formfile, user=request.user)
                        f.name = f.filename()
                        f.save()
                return redirect('filesharing:My_Files')
            else:
                return render(request, 'filesharing/uploadfile.html', {'form': form})
    else:
            form = DocumentForm(None)
            return render(request, 'filesharing/uploadfile.html', {'form': form})
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
                    return redirect('filesharing:user-linked-files', pk)
        else:
            return render(request, 'filesharing/uploadfile.html', {'form': form})
    else:
        form = DocumentForm(None)
        return render(request, 'filesharing/uploadfile.html', {'form': form})
class FileDelete(DeleteView):
    model = File

    def get_success_url(self):
        f = File.objects.get(pk=self.kwargs['pk'])
        folder = f.folder
        if not folder:
            return reverse('filesharing:My_Files')
        else:
            return reverse_lazy('filesharing:user-linked-files',kwargs={'folder_id': folder.pk})

    def get(self, *args, **kwargs):
            return self.post(*args, **kwargs)


def ousersfile(request,user):
    ruser=User.objects.get(username=user)
    user_folders = Folder.objects.filter(user=ruser)
    user_files = File.objects.filter(user=ruser)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = {'all_folders': all_folders, 'all_files': all_files}
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

    return redirect('filesharing:My_Files')



def makepublic(request,pk):
    user = request.user
    all_files = File.objects.filter(user=user)
    gfile = all_files.get(pk=pk)
    gfile.isprivate = False
    gfile.save(update_fields=["isprivate"])
    all_files = File.objects.filter(user=user)
    context = {'all_files': all_files, 'u': user}
    return redirect('filesharing:My_Files')


# class FolderCreate(LoginRequiredMixin, CreateView):
#     model = Folder
#     fields = ['name']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(FolderCreate,self).form_valid(form)

def nolinkfolder(request):
    if request.method == 'POST':
        form=FolderForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            folder=Folder(name=f.name,user=request.user)
            folder.save()
            return redirect('filesharing:My_Files')

        else:
            return render(request,'filesharing/uploadfolder.html',{'form':form})
    else:
            form=FolderForm(None)
            return render(request,'filesharing/uploadfolder.html',{'form':form})


def Folder_Create(request,pk):


     if request.method == 'POST':
         form = FolderForm(request.POST)
         if form.is_valid():
             f = form.save(commit=False)
             folder = Folder(name=f.name, user=request.user,linkedfolder=Folder.objects.get(pk=pk))
             folder.save()
             return redirect('filesharing:user-linked-files',pk)

         else:
             return render(request, 'filesharing/uploadfolder.html', {'form': form})
     else:
         form = FolderForm(None)
         return render(request, 'filesharing/uploadfolder.html', {'form': form})


def FolderUploadIndex(request):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        p = request.POST['path']
        file_path_list = []
        t = ""
        for i in range(len(p)):
            if p[i]!=" ":
                t = t+p[i]
            else:
                file_path_list.append(t)
                t = ""

        pathlist_list = []

        for path in file_path_list:
            t = ""
            list = []
            for i in range(len(path)):
                if path[i]!='/':
                    t = t + path[i]
                else:
                    list.append(t)
                    t = ""
            pathlist_list.append(list)

        for path in pathlist_list:
            for i in range(len(path)):
                if i==0:
                    try:
                        fol = Folder.objects.get(linkedfolder__isnull=True,name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol
                else:
                    try:
                        fol = Folder.objects.get(linkedfolder=path[i-1],name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=path[i-1],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol


        if form.is_valid():
            index = 0
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    pa = pathlist_list[index]
                    folder = pa[len(pa)-1]
                    f = File(file=formfile,user=request.user,folder=folder )
                    f.name = f.filename()
                    f.save()
                    index = index+1

        return redirect('filesharing:My_Files')
    else:
        form = FolderUploadForm(None)
        return render(request,'filesharing/multiplefiles.html',{'form':form})

def FolderUpload(request,pk):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)

        p = request.POST['path']
        print(p,1)
        file_path_list = []
        t = ""
        for i in range(len(p)):
            if p[i]!=" ":
                t = t+p[i]
            else:
                file_path_list.append(t)
                t = ""

        pathlist_list = []

        for path in file_path_list:
            t = ""
            list = []
            for i in range(len(path)):
                if path[i]!='/':
                    t = t + path[i]
                else:
                    list.append(t)
                    t = ""
            pathlist_list.append(list)

        for path in pathlist_list:
            for i in range(len(path)):
                if i==0:
                    try:
                        link = Folder.objects.get(pk=pk)
                        fol = Folder.objects.get(linkedfolder=link,name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=link,user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol
                else:
                    try:
                        fol = Folder.objects.get(linkedfolder=path[i-1],name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=path[i-1],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol


        if form.is_valid():
            index = 0
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    pa = pathlist_list[index]
                    folder = pa[len(pa)-1]
                    f = File(file=formfile,user=request.user,folder=folder )
                    f.name = f.filename()
                    f.save()
                    index = index+1

        return redirect('filesharing:user-linked-files',pk)
    else:
        form = FolderUploadForm(None)
        return render(request,'filesharing/multiplefiles.html',{'form':form})




