"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users.views import home_view, teacher_dashboard_view, student_dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Главная страница
    path('auth/', include(('users.urls', 'users'), namespace='users')),  # ✅ Пространство имён users
    path('courses/', include('courses.urls')),
    path('teacher/dashboard/', teacher_dashboard_view, name='teacher_dashboard'),
    path('student/dashboard/', student_dashboard_view, name='student_dashboard'),
]
