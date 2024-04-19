from django.contrib import admin
from .models import Course, Teacher, Tag


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    filter_horizontal = ('tags',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname', 'email')


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Tag)
