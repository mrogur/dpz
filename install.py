#!/usr/bin/env python
from pathlib import Path
#import argparse

from dpz.config import ConfigToml, set_project_root
from dpz.dpz import Depozyt

set_project_root(Path(__file__).parent)
# parser = argparse.ArgumentParser(description="Depozyt tool")
# parser.add_argument("")
cfg = ConfigToml()
depozyt = Depozyt(cfg.load())
depozyt.run()
