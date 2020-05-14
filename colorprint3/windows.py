from builtins import print as pythonprint
from os import system
def print(*word,sep=None,end=None,file=None,flush=True,color="white",background="black"):
    dic = {
        "black": "0",
        "red": "1",
        "green": "2",
        "yellow": "3",
        "blue": "4",
        "magenta": "5",
        "cyan": "6",
        "white": "7"
    }
    if (color in dic) and (background in dic) and flush:
        system('echo|set /p=[3'+str(dic[color])+'m')
        system('echo|set /p=[4'+str(dic[background])+'m')
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)
        system('echo|set /p=[0m')
    else :
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)
