import ast

class Configurator(object):
    def __init__(self):
        with open(CONFIG_FILE) as config:
            settings = ast.literal_eval(config.read())
            for key in settings:
            if hasattr(self, key):
                setattr(self, key, settings[key])
