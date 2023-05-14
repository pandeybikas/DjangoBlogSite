from django.shortcuts import render
from home.models import Blog
# Create your views here.
def health(request):
    health_blogs = Blog.objects.filter(category_id=1)
    return render(request, 'health.html', {'health_blogs': health_blogs})



def travel(request):
    travel_blog = Blog.objects.filter(category_id=2)
    return render(request, 'travel.html', {'travel_blog': travel_blog})




def news(request):
    news_blog = Blog.objects.filter(category_id=3)
    return render(request, 'news.html',{'news_blog': news_blog})




def movies(request):
    movie_blog = Blog.objects.filter(category_id=4)
    return render(request, 'movies.html', {'movie_blog': movie_blog})