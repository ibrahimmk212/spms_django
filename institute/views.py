from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from institute.models import Faculty, Department, Session
from institute.serializers import FacultySerializer, DepartmentSerializer, SessionSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing faculty.
    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]



class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing department.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class SessionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing session.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
