from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=100, null=True)
    pic = models.ImageField(upload_to='media', null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    item = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.item    


class Blog(models.Model):
    title= models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    image= models.ImageField(upload_to='media', null=True)
    desc = models.TextField(null=True)
    author= models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    category= models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    publish_date = models.DateField(auto_now=True, null=True)
    approved = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.title