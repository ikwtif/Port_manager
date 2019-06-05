import sys
import os

def load_path():
    #######COMMENT IN FOR PYINSTALLER LINUX#######
    '''
    basedir = sys.executable
    last_dir = basedir.rfind("/")
    basedir = basedir[:last_dir]
    path = '{}/test_port.xlsx'.format(basedir)
    '''
    #######COMMENT IN FOR PYINSTALLER WINDOWS#######
    '''
    path = os.path.dirname(sys.executable)
    ------
    or
    -----
    basedir = sys.executable
    last_dir = basedir.rfind("\\")
    path = basedir[:last_dir]
    '''
    #######COMMENT OUT FOR PYINSTALLER#######
    path = os.path.dirname(os.path.realpath(__file__))
    ##########################################
    return path