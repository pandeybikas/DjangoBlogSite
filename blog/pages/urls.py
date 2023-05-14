from django.urls import path 
from . import views

urlpatterns = [
    path('health', views.health, name='health'),
    path('travel', views.travel, name='travel'),
    path('news', views.news, name='news'),
    path('movies', views.movies, name='movies')
]
