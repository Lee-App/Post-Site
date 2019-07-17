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
    success_url = '/accounts/login'
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password_confirm = form.cleaned_data.get('password_confirm')

        if password == password_confirm:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            return super().form_valid(form)

        return super().form_invalid(form)
        
