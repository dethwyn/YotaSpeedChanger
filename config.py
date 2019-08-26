import os
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if platform.system() == 'Linux':
    WEB_DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver/chromedriver')
elif platform.system() == 'Windows':
    WEB_DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver/chromedriver.exe')