from django.db import models
from datetime import datetime, date


class Car(models.Model):
    vendor = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveIntegerField()


class Fighter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth= models.DateTimeField(null=True)
    age = models.PositiveSmallIntegerField(default=0)
    weight = models.FloatField(null=True)
    growth = models.FloatField(null=True)

class Federation(models.Model):
    options = (
        ('Martial arts','Martial arts   '),
        ('Full contact sports','Full contact sports'),
        ('MMA','MMA'),
        ('Karate','Karate'),
        ('Applied arts','Applied arts'),
    )
    Federation = models.CharField(max_length=20, choices=options)
    directions = models.CharField(max_length=50, default='SOME STRING')

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=40)
    # image = models.ImageField(null=True, blank=True)
    publication_date = models.DateField(null=True)
