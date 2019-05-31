"""Load configuration from environment
"""

import os
import yaml

class Configuration():
    """Parses the environment configuration to create the config objects.
    """

    def __init__(self):
        """Initializes the Configuration class
        """
        with open('defaults.yml', 'r') as config_file:
            default_config = yaml.safe_load(config_file)

        if os.path.isfile('config.yml'):
            with open('config.yml', 'r') as config_file:
                user_config = yaml.safe_load(config_file)
        else:
            user_config = dict()

        if 'settings' in user_config:
            self.settings = {**default_config['settings'], **user_config['settings']}
        else:
            self.settings = default_config['settings']

if __name__ == '__main__':
    conf = Configuration()
    print(conf.settings)