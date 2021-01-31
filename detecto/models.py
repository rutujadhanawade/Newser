from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    summary = models.TextField()
    title = models.TextField(default="")
    accuracy = models.IntegerField(default=0)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()


