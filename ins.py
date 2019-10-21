import os
import sys

def ins():
    plat = sys.platform
    if plat == 'win32':
        os.system('pip install google')
        os.system('pip install wikipedia')
        os.system('pip install chatterbot')
        os.system('pip install youtube-dl')
    elif plat == 'linux':
        os.system('pip3 install google')
        os.system('pip3 install wikipedia')
        os.system('pip3 install chatterbot')
        os.system('pip3 install youtube-dl')
