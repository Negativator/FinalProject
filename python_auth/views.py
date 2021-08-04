from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from python_auth.forms import RegisterForm, ProfileForm, LoginForm
from python_auth.models import UserProfile
from quiz.models import Quiz


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('landing')
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('landing')

        context = {
            'login_form': login_form,
        }
        return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('landing')

@login_required
def profile(request):
   user = request.user
   profile = UserProfile.objects.get(user=user.id)
   context = {
       'user': user,
       'profile': profile,
       'created_quizzes': Quiz.objects.filter(user=user),
   }
   return render(request, 'auth/profile.html', context)