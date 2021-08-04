from django.urls import path

from python_auth.views import register_user, login_user, logout_user, profile

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/', profile, name='user profile'),
)