from django.urls import path

from quiz.views import create_quiz, quiz_overview, add_question

urlpatterns = (
    path('create_quiz/', create_quiz, name='create quiz'),
    path('quiz_overview/<int:pk>/', quiz_overview, name='quiz overview'),
    path('add_question/<int:pk>/', add_question, name='add question'),
)