from django.contrib import admin

from project.models import Allocation, Proposal


@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'supervisor', 'coordinator', 'session')
    ordering = ('supervisor',)
    search_fields = ('student',)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'topic1', 'topic2', 'topic3', 'approval')
    ordering = ('student',)
    search_fields = ('student', )
