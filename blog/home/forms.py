from django import forms 
from .models import Comment

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