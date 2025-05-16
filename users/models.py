from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Кастомная модель пользователя с ролями:
    - Студент
    - Преподаватель
    - Администратор
    """
    class Role(models.TextChoices):
        STUDENT = 'student', 'Студент'
        TEACHER = 'teacher', 'Преподаватель'
        ADMIN = 'admin', 'Администратор'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name='Роль пользователя',
        db_index=True  # Индекс для ускорения поиска по роли
    )

    # При необходимости можно добавить аватар
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
