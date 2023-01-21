from django.contrib import admin
from django.urls import path

from account.views import UsersList, UsersDetail

urlpatterns = [
    path('<str:userstype>/', UsersList.as_view(), name='users list'),
    path('user/<int:pk>/', UsersDetail.as_view(), name='users detail'),
]