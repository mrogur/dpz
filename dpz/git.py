import shutil
import subprocess
import os.path as p


class Git:
    def __init__(self, dirs: dict):
        self.dirs = dirs

    def clone(self, repo_base_url, repo_name):
        realpath = p.realpath(f'{self.dirs["src"]}/{repo_name}')
        shutil.rmtree(realpath, ignore_errors=True)
        command = f'git clone {repo_base_url}/{repo_name}.git "{realpath}"'
        subprocess.call(command, shell=True)
