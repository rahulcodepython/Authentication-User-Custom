from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")