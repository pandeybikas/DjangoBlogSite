from django.db import models

# Create your models here.
class Category(models.Model):
    item = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.item    


class Blog(models.Model):
    title= models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    image= models.ImageField(upload_to='media', null=True)
    desc = models.TextField(null=True)
    author= models.CharField(max_length=100, null=True)
    author_pic = models.ImageField(upload_to='media', null=True)
    author_bio= models.TextField(null=True)
    category= models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    publish_date = models.DateField(auto_now=True, null=True)
    approved = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment_on = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name