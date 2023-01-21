from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, AbstractUser)
from django.db import models

from institute.models import Department, Session, Faculty


class AccountManager(BaseUserManager):
    def create_user(self, full_name, email, id_number, phone, role, username=None, password=None):
        if not full_name:
            return ValueError("Name is required")
        if not email:
            return ValueError("email is required")
        if not id_number:
            return ValueError("id number is required")
        if not phone:
            return ValueError("phone number is required")

        user = self.model(
            full_name=full_name,
            email=email,
            id_number=id_number,
            phone=phone,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, id_number,  phone, role=5, username=None, password=None):
        user = self.create_user(
            full_name=full_name,
            email=email,
            id_number=id_number,
            phone=phone,
            role=role
        )

        user.set_password(phone)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    USER_TYPE_CHOICES = (
            (1, 'student'),
            (2, 'supervisor'),
            # (3, 'external_supervisor'),
            (4, 'coordinator'),
            (5, 'admin')
        )

    title = models.CharField(verbose_name='Title', max_length=200, null=True, blank=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=200, null=True)
    id_number = models.CharField(verbose_name='ID Number', max_length=200, unique=True)
    email = models.CharField(verbose_name='Email', max_length=200, unique=True, null=True)
    phone = models.CharField(verbose_name='Phone', max_length=200, unique=True, null=True)
    password = models.CharField(max_length=225, unique=False)
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    objects = AccountManager()

    def __str__(self):
        return self.full_name

    USERNAME_FIELD = 'id_number'
    REQUIRED_FIELDS = ['full_name', 'email', 'phone']


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



