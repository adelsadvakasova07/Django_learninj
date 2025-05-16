from django.urls import path
from .views import course_list_view, course_detail_view, course_create_view

app_name = 'courses'

urlpatterns = [
    path('', course_list_view, name='course_list'),                 # Список курсов
    path('create/', course_create_view, name='course_create'),      # Создание курса
    path('<int:course_id>/', course_detail_view, name='course_detail'),  # Детали курса
]
