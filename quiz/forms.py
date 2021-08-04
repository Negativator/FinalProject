from django import forms

from quiz.models import Quiz, Question


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ('user',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'c1', 'c2', 'c3', 'c4', 'correct_answer')
