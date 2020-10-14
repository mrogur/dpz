import toml
import os.path as p


class ConfigToml:
    def __init__(self, config_path="dpz.toml"):
        self.config_path = config_path

    def load(self):
        pth = p.realpath(self.config_path)
        return toml.load(pth)