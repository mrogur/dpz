from unittest import TestCase
import os.path as p

from bs import GradleGroovyDsl


class TestGradle(TestCase):
    def test_parse_version(self):
        g = GradleGroovyDsl(p.realpath(""), 'gradle-multi')
        g.parse_version()
        self.assertEqual("1.0-SNAPSHOT", g.version)

    def test_parse_submodules(self):
        g = GradleGroovyDsl(p.realpath(""), 'gradle-multi')
        self.assertTrue(g.parse_submodules())
