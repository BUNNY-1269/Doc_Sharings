from django.urls import path
from .import views


urlpatterns = [
      path('home1',views.home1,name='home1'),
      path('allusers',views.allusers,name='allusers'),
      path('My_Files',views.My_Files,name='My_Files'),
      path('uploadfile',views.uploadfile,name='uploadfile'),
      path('<slug:user>',views.ousersfile,name='ousersfiles'),
      path('My_Files/<int:pk>',views.delete,name='delete'),
      path('My_Files/makeprivate/<int:pk>',views.makeprivate,name='makeprivate'),
      path('My_Files/makepublic/<int:pk>',views.makepublic,name='makepublic')
]
