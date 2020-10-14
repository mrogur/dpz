import os
from pathlib import Path


class BuildSystem:
    def __init__(self, absolute_path: str, build_file_name: str):
        self.absolute_path = absolute_path
        self.build_file_name = build_file_name

    def build(self):
        pass

    def is_module_root(self):
        pass

    def get_modules(self):
        pass

    def get_version(self):
        pass


def get_build_system(absolute_path: str) -> BuildSystem:
    if has_file(absolute_path, "pom.xml"):
        return Maven(absolute_path, "pom.xml")
    if has_file(absolute_path, "build.gradle"):
        return GradleGroovyDsl(absolute_path, "build.gradle")
    if has_file(absolute_path, "build.gradle.kts"):
        return GradleKotlinDsl(absolute_path, "build.gradle.kts")


def has_file(absolute_path: str, file_name) -> bool:
    pth = os.path.join(absolute_path, file_name)
    p = Path(pth)
    return p.exists()


class Maven(BuildSystem):

    def build(self):
        pass


class Gradle(BuildSystem):
    def build(self):
        pass


class GradleGroovyDsl(Gradle):
    def build(self):
        pass


class GradleKotlinDsl(Gradle):
    def build(self):
        pass
