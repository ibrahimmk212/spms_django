from rest_framework import serializers

from account.serializer import AccountSerializer
from project.models import Allocation


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['student', 'supervisor', 'coordinator']
        depth=1


class AllocationReadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['id', 'student', 'supervisor', 'coordinator']
