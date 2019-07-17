from django import forms
from django.contrib.auth.models import User

class UserSignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }