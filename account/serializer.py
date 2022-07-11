from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'title',
                  'full_name',
                  'id_number',
                  'email',
                  'phone',
                  'department',
                  'role',
                  'date_joined',
                  'last_login')


