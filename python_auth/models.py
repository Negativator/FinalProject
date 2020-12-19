from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from quiz.models import Quiz


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


