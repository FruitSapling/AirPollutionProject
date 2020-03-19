from django.test import TestCase
from airmap.models import Monitor
from datetime import datetime

class MonitorTests(TestCase):

    # Test that this function returns the expected text
    def test_get_reading_with_time(self):
        dt = datetime(2019, 4, 13, 12, 0, 0, 0)
        monitor = Monitor.objects.create(latest_reading=10, latest_reading_datetime= dt)
        result = monitor.get_reading_with_time()

        expected = "10 last recorded at 2019-04-13 12:00:00"

        self.assertEqual(result, expected)
