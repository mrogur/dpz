from unittest import TestCase
import os.path as p

from dpz.bs import Gradle


class TestGradle(TestCase):
    def test_parse_version(self):
        g = Gradle(p.realpath(""), 'gradle-multi', 'build.gradle')
        g.parse_version()
        self.assertEqual("1.0-SNAPSHOT", g.version)

    def test_parse_submodules(self):
        g = Gradle(p.realpath(""), 'gradle-multi', 'build.gradle')
        self.assertTrue(g.parse_submodules())
