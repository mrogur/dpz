import shutil
import os.path as p

from modules.git import Git


class App:
    def __init__(self, config):
        self.config = config
        self.path = self.__dir__()

    def pull_repositories(self):
        g = Git()
        git_config = self.config['git']
        for package in git_config['packages']:
            repository_url = git_config['repository']
            g.cloneRepo(repository_url, package)

    def unzip_projects(self):
        pass

    def build(self):
        pass

    def clean(self, dest):
        shutil.rmtree(dest, ignore_errors=True)

    def run(self):
        print(self.config)
        print(self.path)
        self.pull_repositories()
        self.unzip_projects()
        self.build()
