from django.urls import path
from .import views


urlpatterns = [
      path('', views.home, name='home'),
      path('login',views.login,name='login'),
      path('register',views.register,name='register'),
      path('logout',views.logout,name='logout'),
      path('profile',views.profiles,name='profile'),
      path('profileupdate',views.profileupdate,name='profileupdate'),
      path('createdprofile',views.createdprofile,name='createdprofile'),
      path('alreadythere',views.alreadythere,name='alreadythere'),
      path('oprofile/<slug:user>', views.oprofile, name='oprofile')
]

