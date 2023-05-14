from django.shortcuts import render
from home.models import Blog
from django.core.paginator import Paginator
# Create your views here.
def health(request):
    health_blogs = Blog.objects.filter(category_id=1)
    pagination = Paginator(health_blogs, 6)
    page_number = request.GET.get('page')
    health_blogs= pagination.get_page(page_number)
    return render(request, 'health.html', {'health_blogs': health_blogs})



def travel(request):
    travel_blog = Blog.objects.filter(category_id=2)
    pagination = Paginator(travel_blog, 6)
    page_number = request.GET.get('page')
    travel_blog = pagination.get_page(page_number)
    return render(request, 'travel.html', {'travel_blog': travel_blog})




def news(request):
    news_blog = Blog.objects.filter(category_id=3)
    pagination = Paginator(news_blog, 6)
    page_number = request.GET.get('page')
    news_blog= pagination.get_page(page_number)
    return render(request, 'news.html',{'news_blog': news_blog})




def movies(request):
    movie_blog = Blog.objects.filter(category_id=4)
    pagination = Paginator(movie_blog, 6)
    page_number = request.GET.get('page')
    movie_blog= pagination.get_page(page_number)
    return render(request, 'movies.html', {'movie_blog': movie_blog})