#!/usr/bin/env python3

import configparser
from pathlib import Path
import os


CONF = 'fyta.conf'


def load_conf():
    config = configparser.ConfigParser()

    # Try to find ./fyta.conf
    config_path = os.path.join(Path(__file__).parent.resolve(), CONF)
    if not Path.is_file(Path(config_path)):
        raise f'No config located in {config_path}'

    config.read(config_path)

    return config
