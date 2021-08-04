from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    form_title = models.CharField(max_length=1000)
    form_description = models.CharField(max_length=2000)
    total_questions = models.IntegerField(null=True)

    def __str__(self):
        return self.form_title


class Question(models.Model):
    ANSWER_CHOICE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    title = models.CharField(max_length=1000, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    c1 = models.CharField(max_length=1000, blank=False, verbose_name='A')
    c2 = models.CharField(max_length=1000, blank=False, verbose_name='B')
    c3 = models.CharField(max_length=1000, blank=False, verbose_name='C')
    c4 = models.CharField(max_length=1000, blank=False, verbose_name='D')
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICE, default='A')

    def __str__(self):
        return self.title


