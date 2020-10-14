import os
import shutil
import pprint as pp
import zipfile
import os.path as p
from modules.git import Git


class App:
    def __init__(self, config):
        self.config = config

    def pull_repositories(self):
        g = Git()
        git_config = self.config['git']
        for package in git_config['packages']:
            repository_url = git_config['repository']
            print(f"Cloning repo: {repository_url}")
            g.cloneRepo(repository_url, package)

    @staticmethod
    def unzip_projects():
        for zip_file in os.listdir(p.realpath("zip")):
            if not zip_file.endswith(".zip"):
                continue

            zip_path = p.realpath(f"zip/{zip_file}")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(p.realpath("src"))

    def build(self):
        pass

    def clean(self, dest):
        shutil.rmtree(dest, ignore_errors=True)

    def prepare_sources(self):
        pp.pprint(self.config)
        # self.pull_repositories()
        self.unzip_projects()

    def run(self):
        self.prepare_sources()