from django.shortcuts import render

from rest_framework.decorators import action
from institute.models import Session
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from project.models import Allocation, Proposal, Grading, ChapterApproval
from project.serializers import AllocationSerializer, AllocationReadWriteSerializer, ChapterApprovalSerializer, GradingRWSerializer, ProposalSerializer, GradingSerializer
from account.models import Account


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


class ProposalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Allocation.
    """
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    @action(methods=['post'], detail=False)
    def create_or_update(self, request):
        student = request.data.get('student')
        try:
            proposal = Proposal.objects.get(student=student)
            serializer = self.get_serializer(proposal, data=request.data, partial=True)
        except Proposal.DoesNotExist:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ChapterApprovalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Allocation.
    """
    queryset = ChapterApproval.objects.all()
    serializer_class = ChapterApprovalSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class GradingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Grading.
    """
    queryset = Grading.objects.all()
    serializer_class = GradingSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class GradingRWViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Grading.
    """
    queryset = Grading.objects.all()
    serializer_class = GradingRWSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class GenerateProposalViewSet(viewsets.ModelViewSet):

    """
    A simple ViewSet for viewing and editing Allocation.
    """
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

    def create(self, request, *args, **kwargs):
        students = Account.objects.filter(role=1)
        supervisors = Account.objects.filter(role=2)
        coordinator = Account.objects.filter(role=5).first()
        session = Session.objects.filter(active=True).first()
        Allocation.objects.all().delete()

        # Divide the students evenly among the supervisors
        allocation = [[] for _ in range(len(supervisors))]
        for i, student in enumerate(students):
            allocation[i % len(supervisors)].append(student)

        # Create the allocations in the database
        for i, supervisor in enumerate(supervisors):
            for student in allocation[i]:
                Allocation.objects.create(
                    student=student,
                    supervisor=supervisor,
                    coordinator=coordinator,
                    session=session
                )
        return Response({'success': "Allocation Generated Successfully"}, status=status.HTTP_201_CREATED)

    # permission_classes = [IsAuthenticatedOrReadOnly]


class CountView(APIView):
    def get(self, request, format=None):
        coordinators = Account.objects.filter(role=4).count()
        supervisors = Account.objects.filter(role=2).count()
        students = Account.objects.filter(role=1).count()
        projects = (Proposal.objects.filter(approval=1) or Proposal.objects.filter(approval=2) or
                    Proposal.objects.filter(approval=3)).count()

        data = {
            'coordinators': coordinators,
            'supervisors': supervisors,
            'students': students,
            'projects': projects
        }
        return Response(data)


class StudentProposalView(APIView):
    def get(self, request, student_id):
        proposal = get_object_or_404(Proposal, student=student_id)
        serializer = (ProposalSerializer(proposal))
        return Response(serializer.data)


class StudentMyDetailView(APIView):
    def get(self, request, student_id):
        detail = get_object_or_404(Allocation, student=student_id)
        serializer = AllocationSerializer(detail)
        return Response(serializer.data)


class ChapterApprovalUpdateView(APIView):     
    def get(self, request, proposal):
        chapters = get_object_or_404(ChapterApproval, proposal=proposal)
        serializer = ChapterApprovalSerializer(chapters)
        return Response(serializer.data, status=200)


