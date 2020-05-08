import sys,platform
from os import system
if ('idlelib.run' not in sys.modules) and (platform.system() == 'Windows') and (platform.release() == '10') :
    from .windows import *
elif (platform.system() == 'Linux') :
    from .ubuntu import *
else :
    print('Not Support for IDLE or Unsupported OS')
    exit()
