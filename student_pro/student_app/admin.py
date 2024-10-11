from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'is_enrolled', 'enrollment_date', 'GPA')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_enrolled', 'enrollment_date', 'GPA')

