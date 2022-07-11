from django.db import models

from account.models import Account
from institute.models import Session


class Allocation(models.Model):
    student = models.ForeignKey(Account, related_name="student", on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Account, related_name="supervisor", on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Account, related_name="coordinator", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name='Session', on_delete=models.CASCADE)


    def __str__(self):
        return self.session


# class Topic(models.Model):
#     title = models.TextField(max_length=300)
#     allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
#     progress = models.TextField(max_length=200)
#     score = models.ForeignKey(Account, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title