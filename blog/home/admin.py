from django.contrib import admin
from .models import  Category, Blog, Comment
# Register your models here.
class ModelBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']
    prepopulated_fields = {'slug' : ('title',)}
admin.site.register(Blog, ModelBlogAdmin)
admin.site.register(Category)

admin.site.register(Comment)