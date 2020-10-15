from unittest import TestCase
import os.path as p
from bs.bs import Gradle


class TestGradle(TestCase):
    def test_parse_metadata(self):
        g = Gradle(p.realpath("."), 'gradle-multi', 'build.gradle')
        g.parse_metadata()
