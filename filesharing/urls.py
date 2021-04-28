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
      path('uploadlinkedfile/<int:pk>',views.uploadlinkedfile,name='uploadlinkedfile'),
      path('<int:folder_id>/', views.detail, name='detail'),
      path('folder_upload/<int:pk>/', views.FolderUpload, name='folder-upload'),
      path('folder_upload_index/', views.FolderUploadIndex, name='folder-upload-index'),
      path('folder/add/', views.FolderCreate.as_view(), name='folder-add'),
      path('folder/add/<int:pk>',views.Folder_Create,name='linked-folder-add')

]
