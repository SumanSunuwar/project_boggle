from django.db import models

class Game(models.Model):
    score = models.PositiveIntegerField()
    