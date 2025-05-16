from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # <-- Используем твою модель

# Форма регистрации с выбором роли
class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.Role.choices, label='Роль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']


# Форма входа
class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
