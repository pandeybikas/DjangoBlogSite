from django import forms 
from .models import Comment, Blog
from django.utils.text import slugify
class BlogModelForm(forms.ModelForm):
    slug= forms.SlugField(
        label= "slug",
        widget= forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )
    class Meta:
        model = Blog
        fields = ['title', 'image', 'desc', 'author', 'author_pic', 'author_bio', 'category', 'slug']
        exclude = ['publish_date', 'approved']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

        





class CommentModelForm(forms.ModelForm):
    name= forms.CharField(
        label= 'Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'type' : 'text'
        })
    )
    body= forms.CharField(
        label= 'Comment',
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'type' : 'text',
            'rows' : 5
        })
    )
    class Meta:
        model = Comment
        fields = ['name', 'body']
        exclude = ['comment_on', 'date']