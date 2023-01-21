from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Faculties'


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
