from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import View

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/profile.html')
        
    def post(self, request, *args, **kwargs):
        return self.get(request)

from .forms import UserSignUpForm
from django.views.generic import FormView

class SignUpView(FormView):
    success_url = '/post/list'
    template_name = ''
