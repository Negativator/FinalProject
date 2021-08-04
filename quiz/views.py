from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from quiz.forms import QuizForm, QuestionForm
from quiz.models import Quiz, Question


@login_required
def create_quiz(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'quiz_form': QuizForm(),
            'user': request.user,
        }
        return render(request, 'quiz/create_quiz.html', context)
    else:
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.user = user
            quiz.save()
            return redirect(f'../quiz_overview/{quiz.pk}')

        context = {
            'quiz_form': quiz_form,
        }
        return render(request, 'quiz/create_quiz.html', context)


def quiz_overview(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'quiz': quiz,
            'questions': Question.objects.filter(quiz=pk),
            'counter': [x for x in range(1, len(Question.objects.filter(quiz=pk)) + 1)],
        }

        return render(request, 'quiz/quiz_overview.html', context)


def add_question(request, pk):
    form = QuestionForm()
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': form,
        }
        return render(request, 'quiz/add_question.html', context)
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect(f'../../quiz_overview/{pk}')
