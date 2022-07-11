from django.contrib import admin

from project.models import Allocation


@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'supervisor', 'session')
    ordering = ('supervisor',)
    search_fields = ('student',)
