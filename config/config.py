import json
import os


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


def get_config(file_name):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)) as f:
        config = json.load(f)
    return config


class CommonConfig:
    def __init__(self):
        self.config = get_config("common.json")

    def get_config(self):
        return self.config


@Singleton
class DbestConfig(CommonConfig):
    def __init__(self):
        CommonConfig.__init__(self)
        self.config.update(get_config("dbest.json"))
        self.config['output_dir'] = os.path.join(self.config["output_dir"], "dbest")
        os.makedirs(self.config['output_dir'], exist_ok=True)

