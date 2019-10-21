import os
import sys

def ins():
    plat = sys.platform
    if plat == 'win32':
        os.system('pip install google')
        os.system('pip install wikipedia')
        os.system('pip install chatterbot')
        
    elif plat == 'linux':
        os.system('pip3 install google')
        os.system('pip3 install wikipedia')
        os.system('pip3 install chatterbot')
        
