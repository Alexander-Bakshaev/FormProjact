from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
