import os
import re
import xml.etree.ElementTree
from pathlib import Path


class BuildSystem:
    def __init__(self, absolute_path: str, module_name: str, build_file_name: str):
        self.module_name = module_name
        self.absolute_path = absolute_path
        self.build_file_name = build_file_name
        self.build_file_path = os.path.join(absolute_path, build_file_name)
        self.module_root = None
        self.version = None
        self.project_name = None
        self.submodules = []

    def build(self):
        pass

    def is_module_root(self):
        pass

    def parse_metadata(self):
        pass

    def get_modules(self) -> list:
        if self.project_name is None:
            self.parse_metadata()

        if self.is_module_root():
            return [self]
        # return ModulesFactory.get_build_system(os.path.join(self.absolute_path, self.module_name))

    def get_version(self):
        pass


class ModulesFactory:
    @staticmethod
    def get_build_system(absolute_path: str, module_name: str) -> list:
        if has_file(absolute_path, "pom.xml"):
            return Maven(absolute_path, module_name).get_modules()
        if has_file(absolute_path, "build.gradle"):
            return GradleGroovyDsl(absolute_path, module_name).get_modules()
        if has_file(absolute_path, "build.gradle.kts"):
            return GradleKotlinDsl(absolute_path, module_name).get_modules()


def has_file(absolute_path: str, file_name) -> bool:
    pth = os.path.join(absolute_path, file_name)
    p = Path(pth)
    return p.exists()


class Maven(BuildSystem):

    def __init__(self, absolute_path: str, module_name: str):
        super().__init__(absolute_path, module_name, "pom.xml")

    def is_module_root(self):
        if self.module_root is None:
            return self.module_root

    def parse_metadata(self):
        tree = xml.etree.ElementTree.parse(self.build_file_path)
        root = tree.getroot()
        r = root.tag.rindex('}')
        n = root.tag[:r + 1]

        self.version = tree.findtext(f"{n}version")
        self.project_name = tree.findtext(f"{n}artifactId")
        modules = root.find(f"{n}modules")

        if modules is None:
            self.module_root = True
            return

        self.submodules = [m for m in modules.findall(f"{n}module")]

    def build(self):
        pass


class Gradle(BuildSystem):
    def __init__(self, absolute_path: str, module_name: str, build_file_name: str):
        super().__init__(absolute_path, module_name, build_file_name)
        self.gradle_settings = None
        self.version_pattern = None
        self.module_pattern = None

    def parse_metadata(self):
        self.parse_version()
        self.make_submodules(self.parse_submodules())

    def parse_version(self):
        with open(self.build_file_path) as f:
            conf = f.read()
            m = re.search(self.version_pattern, conf)
            if m is not None:
                self.version = m.group(1)

    def parse_submodules(self):
        with open(os.path.join(self.absolute_path, self.build_file_name)) as f:
            conf = f.read()
            return [m.group(1) for m in re.finditer(self.module_pattern, conf)]

    def build(self):
        pass

    def make_submodules(self, parsed_submodules):
        for m in parsed_submodules:
            self.submodules.append(ModulesFactory.get_build_system(os.path.join(self.absolute_path, m), m))


class GradleGroovyDsl(Gradle):
    def __init__(self, absolute_path: str, module_name: str):
        super().__init__(absolute_path, module_name, "build.gradle")
        self.gradle_settings = "settings.gradle"
        self.version_pattern = "version\\s+[\'\"]+(.*)[\'\"]+"
        self.module_pattern = "include\\s+[\'\"]+(.*)[\'\"]+"


class GradleKotlinDsl(Gradle):
    def __init__(self, absolute_path: str, module_name: str):
        super().__init__(absolute_path, module_name, "build.gradle.kts")
        self.gradle_settings = "settings.gradle.kts"
        self.version_pattern = "version\\s*=\\s*[\'\"]+(.*)[\'\"]+"
        self.module_pattern = "include\\(\\s*[\'\"]+(.*)[\'\"]+\\s*\\)"
