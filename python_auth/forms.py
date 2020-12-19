from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from python_auth.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'created_quizzes')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )