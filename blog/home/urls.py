from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogDetail/<slug>', views.blogDetail, name='blog-detail'),
    path('blogDetail/<slug>/addComment', views.addComment, name='add-comment')
]
