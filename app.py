from flask import Flask

from pyfladesk import init_gui

UPLOAD_FOLDER = '/home/ikwtif/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from __init__ import *


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
	#init_gui(app)