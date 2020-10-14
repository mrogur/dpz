from modules.config import ConfigToml
from modules.app import App

if __name__ == '__main__':
    s = ConfigToml()
    config = s.load()
    app = App(config)
    app.run()
