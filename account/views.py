from account.models import Account
from account.serializer import AccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SupervisorsList(APIView):
    # List all supervisors, or create a new user.
    def get(self, request, userstype, format=None):
        if userstype == 'students':
            users = Account.objects.filter(role=1)
        elif userstype == 'supervisors':
            users = Account.objects.filter(role=2)
        elif userstype == 'externalsupervisors':
            users = Account.objects.filter(role=3)
        elif userstype == 'coordinators':
            users = Account.objects.filter(role=4)
        elif userstype == 'admins':
            users = Account.objects.filter(role=5)

        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, userstype, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupervisorsDetail(APIView):
        # Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


