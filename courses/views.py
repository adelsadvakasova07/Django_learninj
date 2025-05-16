from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Comment
from .forms import CourseForm, CommentForm


# Список всех курсов
def course_list_view(request):
    courses = Course.objects.select_related('teacher').all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# Детальный просмотр конкретного курса + комментарии
@login_required
def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    comments = course.comments.select_related('user').order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.course = course
            comment.user = request.user
            comment.save()
            return redirect('courses:course_detail', course_id=course.id)
    else:
        comment_form = CommentForm()

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'comments': comments,
        'comment_form': comment_form
    })


# Создание курса (только для преподавателей)
@login_required
def course_create_view(request):
    if request.user.role != 'teacher':
        return redirect('courses:course_list')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('courses:course_detail', course_id=course.id)
    else:
        form = CourseForm()

    return render(request, 'courses/course_create.html', {'form': form})
