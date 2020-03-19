from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from airmap.models import Monitor

default_geom = {
  "type":"Point",
  "coordinates":[
    -1.4058208465576172,
    47.15301133231325
  ]
}

class AirmapViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a monitor in the database
        pass

    # Ensure that there is a success response when we try to GET the website.
    def test_airmap(self):
        resp = self.client.get('/airmap/')
        self.assertEqual(resp.status_code, 200)

class CreateMonitorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a monitor in the database
        Monitor.objects.create(
            latest_reading=10,
            latest_reading_datetime=datetime.now(),
            geom=default_geom
        )

    def test_view_accepts_post_data(self):
        response = self.client.post(path=reverse("airmap:create"), data={"mac_address": "00:00:00:00:00:00",
                                                                         "latitude": 5.0, "longitude": 5.0})
        self.assertEqual(response.status_code, 200)

    def test_view_creates_monitor(self):
        # Make a POST request aiming to create a monitor with coordinates latitude=5.0, longitude=5.0
        response = self.client.post(path=reverse("airmap:create"), data={"mac_address": "00:00:00:00:00:00",
                                                                         "latitude": 5.0, "longitude": 5.0})
        expected_coordinates = ['5.0', '5.0']
        self.assertEqual(Monitor.objects.last().geom['coordinates'], expected_coordinates)

class UpdateReadingsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a monitor in the database
        Monitor.objects.create(
            latest_reading=10,
            latest_reading_datetime=datetime.now(),
            geom=default_geom
        )

    def test_view_rejects_invalid_header(self):
        response = self.client.post(path=reverse("airmap:update"), data={"xyz": 5.0, "longitude": 5.0, "latitude":5.0})
        self.assertEqual(response.status_code, 400)
