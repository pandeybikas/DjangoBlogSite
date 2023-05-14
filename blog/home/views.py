from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Blog, Comment
from .forms import CommentModelForm
# Create your views here.
def index(request):
    health_blog = Blog.objects.filter(category_id= 1)[0:3]
    travel_blog= Blog.objects.filter(category_id = 2)[0:3]
    news_blog = Blog.objects.filter(category_id = 3)[0:3]
    movie_blog = Blog.objects.filter(category_id = 4)[0:3]
    
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

def addComment(request, slug):
    comment_obj= Blog.objects.get(slug=slug)
    comm_form = CommentModelForm(instance=comment_obj)
    if request.method == 'POST':
        comm_form= CommentModelForm(request.POST, instance=comment_obj)
        if comm_form.is_valid():
            name = request.POST.get('name')
            body = request.POST.get('body')
            date = request.POST.get('date')
            c= Comment(comment_on=comment_obj, name=name, body=body, date=date)
            c.save()
            return redirect(reverse('blog-detail', args=[comment_obj.slug]))
    else:
        comm_form= CommentModelForm(instance=comment_obj)

    context = {
        'comment_obj' : comment_obj,
        'comm_form' : comm_form
    }         

    return render(request, 'add-comment.html',context )