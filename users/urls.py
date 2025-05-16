from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    login_view,
    teacher_dashboard_view,
    student_dashboard_view,logout_view
)
from courses.views import course_list_view, course_detail_view, course_create_view
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Добавь эту строку
    path('teacher/dashboard/', teacher_dashboard_view, name='teacher_dashboard'),
    path('student/dashboard/', student_dashboard_view, name='student_dashboard'),
    path('', course_list_view, name='course_list'),                 # Список курсов
    path('create/', course_create_view, name='course_create'),      # Создание курса
    path('<int:course_id>/', course_detail_view, name='course_detail'),  # Детали курса
]
