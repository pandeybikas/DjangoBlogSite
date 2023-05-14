from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label= 'Enter Username',
        max_length=20,
        min_length= 2,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            
        })
    )
    email = forms.EmailField(
        label= 'Enter Valid Email',
        
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'type' : 'email'
            
        })
    )
    password1 = forms.CharField(
        label= 'Enter Password',
        
        widget= forms.PasswordInput(attrs={
            'class': 'form-control',
            'type' : 'password'
            
        })
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        
        widget= forms.PasswordInput(attrs={
            'class': 'form-control',
            'type' : 'password'
            
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileModelForm(forms.ModelForm):
    full_name= forms.CharField(
        label= 'Full Name',
        max_length=20,
        min_length=2,
        error_messages={'required': 'This field is mandatory'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text'
        })
    )
    phone= forms.CharField(
        label= 'Phone Number',
        max_length=12,
        min_length=2,
        error_messages={'required': 'This field is mandatory'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'number'
        })
    )
    image= forms.FileField(
        label= 'Upload Image',
        
        error_messages={'required': 'This field is mandatory'},
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/png, image/jpeg',
            'type' : 'file'
        })
    )
    address= forms.CharField(
        label= 'City Name',
        
        error_messages={'required': 'This field is mandatory'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text'
        })
    )
    bio= forms.CharField(
        label= 'About Yourself',
        
        error_messages={'required': 'This field is mandatory'},
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'rows': 5
        })
    )
    class Meta:
        model = Profile
        fields = ['full_name', 'phone', 'image', 'address', 'bio']
        exclude = ['user']
