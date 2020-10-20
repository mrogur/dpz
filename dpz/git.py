import shutil
import subprocess
import os.path as p
from pathlib import Path


class Git:
    def __init__(self, dirs: dict):
        self.dirs = dirs

    def clone(self, repo_base_url: str, repo_name: str, omit_existing: bool):
        realpath = p.realpath(f'{self.dirs["src"]}/{repo_name}')
        pth = Path(realpath)

        if pth.exists() and omit_existing:
            return

        shutil.rmtree(realpath, ignore_errors=True)
        command = f'git clone {repo_base_url}/{repo_name}.git "{realpath}"'
        subprocess.call(command, shell=True)
