from rest_framework import serializers

from institute.models import Faculty, Department, Session


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'faculty']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
