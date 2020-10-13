from django.contrib import admin
from .models import Student
from .models import Teacher

# Register your models here.

#
class CustomeStudent(admin.ModelAdmin):
    list_display = ('sname','teacher')

admin.site.register(Student,CustomeStudent)
admin.site.register(Teacher)
