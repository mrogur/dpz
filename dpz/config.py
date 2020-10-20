from pathlib import Path

import toml
import os.path as p

PROJECT_ROOT = Path(__file__).parent.parent


def set_project_root(root):
    PROJECT_ROOT = root


class ConfigToml:
    def __init__(self, config_path="dpz.toml"):
        self.config_path = config_path

    def load(self):
        pth = p.realpath(self.config_path)
        return toml.load(pth)
