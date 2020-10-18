import os
import shutil
import pprint as pp
import zipfile
import os.path as p

from src.bs import ModulesFactory
from src.config import ConfigToml
from src.git import Git


class Depozyt:
    def __init__(self, configuration):
        self.config = configuration
        self.src_path = p.realpath("src")

    def pull_repositories(self):
        g = Git(self.config['dirs'])
        git_config = self.config['git']
        for package in git_config['packages']:
            repository_url = git_config['repository']
            print(f"Cloning repo: {repository_url}")
            g.clone(repository_url, package)


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

    def build(self):
        pass

    def clean(self, dest):
        shutil.rmtree(dest, ignore_errors=True)

    def prepare_sources(self):
        pp.pprint(self.config)
        self.pull_repositories()
        self.unzip_projects()

    def setup_directories(self):
        for name in self.config['dirs']:
            directory = p.realpath(self.config["dirs"][name])
            if not p.isdir(directory):
                os.mkdir(directory)

    def collect_modules(self) -> list:
        out = []
        for directory in os.listdir(p.realpath(self.config["dirs"]["src"])):
            print(f"Processing {directory}")
            out.append(ModulesFactory.get_build_system(os.path.join(self.src_path, directory), directory))
        return out

    def run(self):
        self.setup_directories()
        self.prepare_sources()
        self.collect_modules()


if __name__ == '__main__':
    s = ConfigToml()
    config = s.load()
    app = Depozyt(config)
    app.run()
