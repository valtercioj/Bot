import os
import sys

def ins():
    plat = sys.platform
    if plat == 'win32':
        try:
            import google
            import wikipedia
            import chatterbot
        except:
            os.system('pip install google')
            os.system('pip install wikipedia')
            os.system('pip install chatterbot')
        
    elif plat == 'linux':
        try:
            import google
            import wikipedia
            import chatterbot
        except:
            os.system('pip3 install google')
            os.system('pip3 install wikipedia')
            os.system('pip3 install chatterbot')
        
