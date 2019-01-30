from django.db import models
from django.utils import timezone

# Create your models here.

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #Position = models.ForeignKey(Position,
    #on_delete=models.CASCADE,
    #related_name = "Position")
    birthdate = models.DateField('birthdate')
    platform = models.TextField(max_length=200)



class Position(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=200)


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,
     on_delete=models.CASCADE,
     related_name = "votes",)
    vote_datetime = models.DateTimeField(default=True)
