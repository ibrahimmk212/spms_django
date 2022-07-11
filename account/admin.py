from django.contrib import admin
from django.contrib.auth.hashers import make_password
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Account


class AccountResource(resources.ModelResource):

    # Harshes the password after importing
    def before_import_row(self, row, **kwargs):
        value = row['phone']
        row['password'] = make_password(value)

    class Meta:
        model = Account

        fields = ('id',
                  'title',
                  'full_name',
                  'id_number',
                  'email',
                  'username',
                  'role',
                  'phone',
                  'password'
                  )
        import_id_fields = ('id',)


class AccountAdmin(ImportExportModelAdmin):
    resource_class = AccountResource


admin.site.register(Account, AccountAdmin)
