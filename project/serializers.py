from rest_framework import serializers

from account.serializer import AccountSerializer
from project.models import Allocation, Proposal, Grading, ChapterApproval


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['id', 'student', 'supervisor', 'coordinator', 'session']
        depth = 1


class AllocationReadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['id', 'student', 'supervisor', 'coordinator', 'session']


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'student', 'topic1', 'topic2', 'topic3', 'approval', 'message']


class GradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grading
        fields = ['id', 'student', 'proposal', 'internal', 'external', 'report']
        depth = 1

class ChapterApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterApproval
        fields = '__all__'



class GradingRWSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grading
        fields = ['id', 'student', 'proposal', 'internal', 'external', 'report']
