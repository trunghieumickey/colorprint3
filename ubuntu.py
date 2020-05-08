from builtins import print as pythonprint
from os import system
def print(*word,sep=None,end=None,file=None,flush=True,color="white"):
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
    if (color in dic) and flush:
        system("/bin/echo -ne \"\\e[0;3"+str(dic[color])+"m\"")
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)
        system("/bin/echo -ne \"\\e[0m\"")
    else :
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)
