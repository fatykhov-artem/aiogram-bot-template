import os

import yaml

from settings import ROOT_DIR

class TextManager:

    @staticmethod
    def load(path: str) -> dict:
        """
        get yalm files
        :param path:
        :return yaml_file:
        """
        with open(os.path.join(ROOT_DIR, path)) as line:
            yaml_file = yaml.safe_load(line)
        return yaml_file
