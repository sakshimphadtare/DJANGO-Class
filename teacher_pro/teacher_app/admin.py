from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'hire_date', 'is_active')
    list_filter = ('subject', 'is_active', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    ordering = ('hire_date',)
    list_editable = ('is_active',)

admin.site.register(Teacher, TeacherAdmin)
