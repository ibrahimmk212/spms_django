from django.contrib import admin
from django.urls import path

from account.views import SupervisorsList, SupervisorsDetail

urlpatterns = [
    path('<str:userstype>/', SupervisorsList.as_view(), name='supervisors'),
    path('user/<int:pk>/', SupervisorsDetail.as_view(), name='supervisor'),
]