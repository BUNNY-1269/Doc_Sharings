from django.urls import path
from .import views


urlpatterns = [
      path('home1',views.home1,name='home1'),
      path('allusers',views.allusers,name='allusers'),
      path('My_Files',views.My_Files,name='My_Files')
]