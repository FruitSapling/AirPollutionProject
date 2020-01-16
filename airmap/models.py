from django.contrib.gis.db import models
# from django.contrib.gis.db.models import PointField
from djgeojson.fields import PointField
from django.utils import timezone

default_geom = {
  "type":"Point",
  "coordinates":[
    -1.4058208465576172,
    47.15301133231325
  ]
}

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Monitor(models.Model):
    latest_reading = models.CharField(max_length=30)
    latest_reading_datetime = models.DateTimeField()
    geom = PointField(default=default_geom)

class Reading(models.Model):
    monitor = models.ForeignKey('Monitor', on_delete=models.CASCADE)
    value = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
