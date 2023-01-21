from rest_framework.permissions import IsAuthenticated

from account.models import Account
from account.serializer import AccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


class UsersList(APIView):
    # permission_classes = (IsAuthenticated)
    # List all supervisors, or create a new user.
    def get(self, request, userstype, format=None):
        users = {}
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
        elif userstype == 'all':
            users = Account.objects.filter()

        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, userstype, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):

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


@receiver(pre_save, sender=Account)
def hash_password(sender, instance, **kwargs):
    if instance.phone:
        if instance.pk is None:
            instance.password = make_password(instance.phone)


