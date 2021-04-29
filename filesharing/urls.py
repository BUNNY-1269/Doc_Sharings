from django.urls import path
from .import views

app_name='filesharing'
urlpatterns = [
      path('home1',views.home1,name='home1'),
      path('allusers',views.allusers,name='allusers'),
      path('My_Files',views.My_Files,name='My_Files'),
      path('uploadfile',views.uploadfile,name='uploadfile'),
      path('<slug:user>',views.ousersfile,name='ousersfiles'),
      path('My_Files/<int:pk>',views.FileDelete.as_view(),name='delete'),
      path('My_Files/makeprivate/<int:pk>',views.makeprivate,name='makeprivate'),
      path('My_Files/makepublic/<int:pk>',views.makepublic,name='makepublic'),
      path('folder/<int:pk>/uploadlinkedfile',views.uploadlinkedfile,name='uploadlinkedfile'),
      path('o/<int:folder_id>/', views.insidefolders, name='detail'),
      path('folder_upload/<int:pk>/', views.FolderUpload, name='folder-upload'),
      path('folder_upload_index/', views.FolderUploadIndex, name='folder-upload-index'),
      path('folder/add/', views.nolinkfolder, name='folder-add'),
      path('folder/add/<int:pk>',views.Folder_Create,name='linked-folder-add'),
      path('folder/<int:folder_id>/', views.user_details, name='user-linked-files'),
      path('My_Folder/<int:pk>',views.FolderDelete.as_view(), name='folder-delete'),
      path('download_folder/<int:pk>/',views.download_folder,name='download_folder'),
      path('<int:pk>/',views.starredfile,name='starredfile'),
      path('remove/<int:pk>/',views.removestar,name='removestar'),
      path('stay/<int:pk>/',views.removestarstay,name='removestay'),
      path('starfolder/<int:pk>/',views.starredfolder,name='starredfolder'),
      path('folder/remove/<int:pk>/',views.removestarfolder,name='removestarfolder'),
      path('folder/stay/<int:pk>/',views.removestarstayfolder,name='removestayfolder'),

]
