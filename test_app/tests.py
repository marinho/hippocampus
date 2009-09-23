from django.test import TestCase
from test_app.models import Widget
from hippocampus.models import *


class LogVisitTestCase(TestCase):
    def setUp(self):
        pass

    def test_track_with_object_id(self):
        self.fail()

    def test_track_with_slug(self):
        self.fail()

    def test_no_track_with_ip_filter(self):
        self.fail()

    def test_detect_ip_address(self):
        self.fail()

    def test_detect_language(self):
        self.fail()

    def test_unique_visits_vs_total(self):
        self.fail()

    def test_obtain_geo_data(self):
        self.fail()
