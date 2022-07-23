from django.db import models

from account.models import Account
from institute.models import Session


class Allocation(models.Model):
    student = models.ForeignKey(Account, related_name="student", on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Account, related_name="supervisor", on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Account, related_name="coordinator", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name='Session', on_delete=models.CASCADE)

    def __str__(self):
        return self.student.full_name


    def __str__(self):
        return self.student


class Proposal(models.Model):
    TOPIC_APPROVAL = (
            (0, 'not_approved'),
            (1, 'topic_1'),
            (2, 'topic_2'),
            (3, 'topic_3'),
            (4, 'rejected'),
    )
    student = models.ForeignKey(Account, on_delete=models.CASCADE, max_length=300)
    topic1 = models.TextField(max_length=300)
    topic2 = models.TextField(max_length=300)
    topic3 = models.TextField(max_length=300)
    message = models.TextField(max_length=300, blank=True)
    approval = models.PositiveSmallIntegerField(choices=TOPIC_APPROVAL, default=0)

    def __str__(self):
        return self.student.full_name