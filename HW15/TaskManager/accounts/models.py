from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='images')
    phone_number = models.CharField(max_length=11)
    
    