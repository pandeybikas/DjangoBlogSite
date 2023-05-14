from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True, null=True)
    full_name= models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    image= models.ImageField(upload_to='media', null=True)
    bio = models.TextField(null=True)
    address = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.user.username