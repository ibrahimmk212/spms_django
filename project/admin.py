from django.contrib import admin

from project.models import Allocation, Proposal, Grading, ChapterApproval


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


@admin.register(Grading)
class GradingAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'proposal', 'internal', 'external', 'report')
    ordering = ('student',)
    search_fields = ('student', )



@admin.register(ChapterApproval)
class ChapterApprovalAdmin(admin.ModelAdmin):
    list_display =  ('id', 'proposal', 'chapter1', 'chapter2', 'chapter3', 'chapter4', 'chapter5')
    ordering = ('proposal',)
    search_fields = ('proposal', )
