#!/usr/bin/env python
from dpz.config import ConfigToml
from dpz.dpz import Depozyt

cfg = ConfigToml()
depozyt = Depozyt(cfg.load())
depozyt.run()
