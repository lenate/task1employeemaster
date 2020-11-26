from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    
    usertype = models.CharField(max_length=50)

class Employees(models.Model):
    
    EmployeeName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Phone=models.IntegerField(default=35354365)
    Email=models.EmailField(max_length=254)
    Image = models.ImageField(upload_to='gallery')