from unittest import TestCase
import os.path as p
from bs.bs import Gradle


class TestGradle(TestCase):
    def test_parse_version(self):
        g = Gradle(p.realpath("."), 'gradle-multi', 'build.gradle')
        g.parse_version()
        self.assertEqual("1.0-SHAPSHOT", g.version)

    def test_parse_submodules(self):
        g = Gradle(p.realpath("."), 'gradle-multi', 'build.gradle')
        g.parse_submodules()
        self.assertTrue(g.submodules)
