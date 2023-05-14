from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    health_blog = Blog.objects.filter(category_id= 1)
    travel_blog= Blog.objects.filter(category_id = 2)
    news_blog = Blog.objects.filter(category_id = 3)
    movie_blog = Blog.objects.filter(category_id = 4)
    
    context = {
        'health_blog' : health_blog,
        'travel_blog' : travel_blog,
        'movie_blog'  : movie_blog,
        'news_blog' : news_blog
    }
    return render(request, 'index.html', context)

def blogDetail(request, slug):
    detail_obj = Blog.objects.get(slug = slug)
    context= {
        'detail_obj' : detail_obj
    }
    return render(request, 'blog-detail.html', context)