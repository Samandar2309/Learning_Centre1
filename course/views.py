from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher


# Create your views here.

def home_view(request):
    courses = Course.objects.all().order_by('-id')[:3]
    teachers = Teacher.objects.all().order_by('id')[:3]
    context = {
        'courses': courses,
        'teachers': teachers
    }
    return render(request, 'index.html', context)


def courselist_view(request):
    courses = Course.objects.all()
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if tag:
        courses = courses.filter(tags__name__icontains=tag)
    if search:
        courses = courses.filter(name__icontains=search)
    context = {
        'courses': courses
    }
    return render(request, 'course.html', context)


def course_detail_view(request, pk):
    course = get_object_or_404(Course, id=pk)
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)


def teacher_detail_view(request, pk):
    teacher = Teacher.objects.get(id=pk)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_detail.html', context)


def teacher_list_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})
