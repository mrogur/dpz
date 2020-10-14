import shutil
import subprocess
import os.path as p

class Git:
    def cloneRepo(self, repo_base_url, repo_name):
        realpath = p.realpath(f'src/{repo_name}')
        shutil.rmtree(realpath, ignore_errors=True)
        command = f'git clone {repo_base_url}/{repo_name}.git "{realpath}"'
        subprocess.call(command, shell=True)
