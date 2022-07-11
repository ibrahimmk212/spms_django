from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from project.models import Allocation
from project.serializers import AllocationSerializer, AllocationReadWriteSerializer


class AllocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Allocation.
    """
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class AllocationReadWriteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Allocation.
    """
    queryset = Allocation.objects.all()
    serializer_class = AllocationReadWriteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]