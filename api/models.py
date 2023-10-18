from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
