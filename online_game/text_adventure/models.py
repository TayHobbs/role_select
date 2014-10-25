from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    health = models.PositiveIntegerField()
    magic = models.PositiveIntegerField()
