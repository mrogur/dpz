from src.config import ConfigToml
from src.dpz import Depozyt

if __name__ == '__main__':
    s = ConfigToml()
    config = s.load()
    app = Depozyt(config)
    app.run()
