from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    place = models.ForeignKey(Place, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('place', 'date')
