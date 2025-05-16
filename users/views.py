from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

# Главная страница
def home_view(request):
    return render(request, 'registration/home.html')

# Регистрация
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_by_role(user)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Вход
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect_by_role(user)
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# Дашборд преподавателя
@login_required
def teacher_dashboard_view(request):
    return render(request, 'dashboards/teacher_dashboard.html')

# Дашборд студента
@login_required
def student_dashboard_view(request):
    return render(request, 'dashboards/student_dashboard.html')

# Перенаправление по роли
def redirect_by_role(user):
    if user.role == 'admin':
        return redirect('/admin/')
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')
    elif user.role == 'student':
        return redirect('student_dashboard')
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')