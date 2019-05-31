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

        if 'log_settings' in user_config:
            self.settings_log = {**default_config['settings_log'], **user_config['settings_log']}
        else:
            self.settings_log = default_config['settings_log']

        if 'main_settings' in user_config:
            self.settings_main = {**default_config['settings_main'], **user_config['settings_main']}
        else:
            self.settings_main = default_config['settings_main']



if __name__ == '__main__':
    conf = Configuration()
    print(conf.settings)