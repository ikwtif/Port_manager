from flask import Flask
from pyfladesk import init_gui
from conf import Configuration
import logs
import structlog

UPLOAD_FOLDER = '/home/ikwtif/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


conf = Configuration()
settings_log = conf.settings_log
settings_main = conf.settings_main
logs.configure_logging(settings_log['log_level'], settings_log['log_mode'])

from __init__ import *


if __name__ == "__main__":

    if settings_main['app']:
        app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
    else:
        init_gui(app, width=1000, height=1000)