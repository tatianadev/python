from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
