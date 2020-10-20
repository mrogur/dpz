from unittest import TestCase
import os.path as p

from bs import GradleGroovyDsl, Maven


class TestGradle(TestCase):
    def test_parse_version(self):
        g = GradleGroovyDsl(p.realpath("gradle-multi"), 'gradle-multi')
        g.parse_version()
        self.assertEqual("1.0-SNAPSHOT", g.version)

    def test_parse_submodules(self):
        g = GradleGroovyDsl(p.realpath("gradle-multi"), 'gradle-multi')
        self.assertTrue(g.parse_submodules())

    def test_make_submodules(self):
        g = GradleGroovyDsl(p.realpath("gradle-multi"), 'gradle-multi')
        g.make_submodules(['gradle-module1', 'gradle-module2'])


class TestMaven(TestCase):
    def test_parse_metadata(self):
        m = Maven(p.realpath("mvn-multi"), "mvn-multi")
        m.make_submodules(["module1", "module2"])
