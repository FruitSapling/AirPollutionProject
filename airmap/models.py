from django.contrib.gis.db import models
from djgeojson.fields import PointField

default_geom = {
  "type":"Point",
  "coordinates":[
    -1.4058208465576172,
    47.15301133231325
  ]
}

class Monitor(models.Model):
    mac_address = models.CharField(max_length=18)
    latest_reading = models.CharField(max_length=30)
    latest_reading_datetime = models.DateTimeField()
    geom = PointField(default=default_geom)

    def get_reading_with_time(self):
        return '{} last recorded at {}'.format(self.latest_reading, self.latest_reading_datetime)

