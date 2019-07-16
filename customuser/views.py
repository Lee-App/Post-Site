from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User

class ProfileView(DetailView):
    model = User
    pk_url_kwarg = 'username'
    template_name = 'registration/profile.html'

from .forms import UserSignUpForm
from django.views.generic import FormView

class SignUpView(FormView):
    success_url = '/post/list'
    template_name = ''
