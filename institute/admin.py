from django.contrib import admin

from institute.models import (Faculty, Department, Session)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faculty')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)
    search_fields = ('name',)
