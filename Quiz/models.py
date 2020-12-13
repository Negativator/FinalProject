from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateField(auto_created=True)


class Section(models.Model):
    name = models.CharField(max_length=100)
    rel_to_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


CHOICES = (
    ('SA', 'Short Answer'),
    ('MC', 'Multiple Choice'),
)


class Question(models.Model):
    title = models.CharField(max_length=100)


class QuestionSA(Question):
    answer = models.CharField(max_length=500)


class QuestionMC(Question):
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
