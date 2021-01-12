import os
import shutil
import pprint as pp
import zipfile
import os.path as p

from .bs import ModulesFactory, BuildSystem
from .config import ConfigToml
from .git import Git


class Depozyt:
    def __init__(self, configuration):
        self.config = configuration
        self.realpath = p.realpath(self.config["dirs"]["src"])
        self.src_path = self.realpath

    def pull_repositories(self, omit_existing: bool):
        g = Git(self.config['dirs'])
        git_config = self.config['git']
        repository_url = git_config['repository']
        print(f"Cloning repo: {repository_url}")
        for package in git_config['packages']:
            g.clone(repository_url, package, omit_existing)

    def unzip_projects(self):
        dirs = self.config["dirs"]
        zip_path = dirs["zip"]
        source_path = dirs["src"]
        for zip_file in os.listdir(p.realpath(zip_path)):
            if not zip_file.endswith(".zip"):
                continue

            zip_path = p.realpath(f"{zip_path}/{zip_file}")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(p.realpath(source_path))

    @staticmethod
    def clean(dest):
        shutil.rmtree(dest, ignore_errors=True)

    def prepare_sources(self):
        pp.pprint(self.config)
        self.pull_repositories(True)
        self.unzip_projects()

    def setup_directories(self):
        for name in self.config['dirs']:
            directory = p.realpath(self.config["dirs"][name])
            if not p.isdir(directory):
                os.mkdir(directory)

    def collect_modules(self) -> list:
        out = []
        for directory in os.listdir(p.realpath(self.config["dirs"]["src"])):
            print(f"appending module {directory}")
            out.append(ModulesFactory.get_build_system(os.path.join(self.src_path, directory), directory))
        return out

    def run(self):
        self.setup_directories()
        self.prepare_sources()
        modules = self.collect_modules()
        self.build(modules)

    def build(self, modules: [BuildSystem]):
        for m in modules:
            print(f"Building module {m.module_name} - {m.version}")
            m.build()


if __name__ == '__main__':
    s = ConfigToml()
    config = s.load()
    app = Depozyt(config)
    app.run()

