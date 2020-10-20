#!/usr/bin/env python
from pathlib import Path

from dpz.config import ConfigToml, PROJECT_ROOT, set_project_root
from dpz.dpz import Depozyt

set_project_root(Path(__file__).parent)

cfg = ConfigToml()
depozyt = Depozyt(cfg.load())
depozyt.run()
