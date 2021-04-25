from django.db import models

# Create your models here.

class movie(models.Model):
    moive_name = models.CharField(max_length=10)
    movie_url = models.URLField(max_length=100)
    movie_num = models.IntegerField()
    movie_access = models.URLField(max_length=100)
    person_see = models.ForeignKey("Person", on_delete=models.CASCADE)

class Person(models.Model):
    name = models.CharField(max_length=10)
