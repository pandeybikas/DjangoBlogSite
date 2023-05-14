from django.urls import path 
from . import views
urlpatterns = [
    path('signUp', views.signUp, name='register'),
    path('signIn', views.signIn, name='login'),
    path('signOut', views.signOut, name='logout'),
    path('profilePage', views.profilePage, name='profile'),
    path('profileEdit/<pk>', views.profileEdit, name='profile-edit')
]
