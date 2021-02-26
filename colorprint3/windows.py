from builtins import print as pythonprint
from os import system
def print(*word,sep=None,end=None,file=None,flush=True,fg_color=None,bg_color=None,style=None):
    foreground_dic = {
        "black": "30", "s_black": "90",
        "red": "31", "s_red": "91",
        "green": "32", "s_green": "92",
        "yellow": "33", "s_yellow": "93",
        "blue": "34", "s_blue": "94",
        "magenta": "35", "s_magenta": "95",
        "cyan": "36", "s_cyan": "96",
        "white": "37", "s_white": "97"
    }
    background_dic = {
        "black": "40", "s_black": "100",
        "red": "41", "s_red": "101",
        "green": "42", "s_green": "102",
        "yellow": "43", "s_yellow": "103",
        "blue": "44", "s_blue": "104",
        "magenta": "45", "s_magenta": "105",
        "cyan": "46", "s_cyan": "106",
        "white": "47", "s_white": "107"
    }
    style_dic = {"bold": "1", "underline": "4",}
    if flush:
        if type(fg_color) == type([]):
            if len(fg_color)==3:
                system('echo|set /p=[38;2;'+str(fg_color[0])+';'+str(fg_color[1])+';'+str(fg_color[2])+'m')
        elif (fg_color in foreground_dic):
            system('echo|set /p=['+str(foreground_dic[fg_color])+'m')
        if type(bg_color) == type([]):
            if len(bg_color)==3:
                system('echo|set /p=[48;2;'+str(bg_color[0])+';'+str(bg_color[1])+';'+str(bg_color[2])+'m')
        elif (bg_color in foreground_dic):
            system('echo|set /p=['+str(background_dic[bg_color])+'m')
        if (style in style_dic):
            system('echo|set /p=['+str(style_dic[style])+'m')
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)
        system('echo|set /p=[0m')
    else :
        pythonprint(*word,sep=sep,end=end,file=file,flush=flush)