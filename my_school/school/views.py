from django.shortcuts import render
from .models import Course,Student,Teacher  # Import your models

def home(request):
    # Query all courses, along with their teachers and students
    # a = Course.objects.all().select_related('teacher').prefetch_related('students')
    
    # context = {
    #     'message': 'Hello, welcome to my school!',
    #     'courses': a ,
# }
    return render(request, 'template.html')
    # , context)
    courses = Course.objects.filter(teacher__subject='Math').select_related('teacher').prefetch_related('students')

context = {
    'message': 'Here are the Math courses!',
    'courses': courses,
}

