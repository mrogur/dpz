import shutil
import pprint as pp

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

    def unzip_projects(self):
        pass

    def build(self):
        pass

    def clean(self, dest):
        shutil.rmtree(dest, ignore_errors=True)

    def prepare_sources(self):
        pp.pprint(self.config)
        self.pull_repositories()
        self.unzip_projects()
