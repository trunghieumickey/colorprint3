from builtins import print as pythonprint
color_dic = {
    "black": "0", "red": "1", "green": "2", "yellow": "3", "blue": "4", "magenta": "5", "cyan": "6", "white": "7"
}
style_dic = {
    "bold": "1", "faint": "2", "italic": "3", "underline": "4"
}
def print(*word, sep=None, end=None, file=None, flush=None, fg_color=None, bg_color=None, style=[]):
    formatlist = []
    if type(fg_color) == type([]):
        if len(fg_color) == 3:
            formatlist.append(38, 2, fg_color)
    elif type(fg_color) == type(""):
        if (fg_color.split('_')[-1] in color_dic):
            if fg_color.split('_')[0] == 's':
                formatlist.append(int("9"+color_dic[fg_color.split('_')[1]]))
            else:
                formatlist.append(int("3"+color_dic[fg_color]))
    if type(bg_color) == type([]):
        if len(bg_color) == 3:
            formatlist.append(48, 2, bg_color)
    elif type(bg_color) == type(""):
        if (bg_color.split('_')[-1] in color_dic):
            if bg_color.split('_')[0] == 's':
                formatlist.append(int("10"+color_dic[bg_color.split('_')[1]]))
            else:
                formatlist.append(int("4"+color_dic[bg_color]))
    if type(style) != type([]):
        style = [style]
    for i in style:
        if i in style_dic:
            formatlist.append(int(style_dic[i]))
    pythonprint(f'\033[',end="")
    pythonprint(*formatlist,sep=";",end="m")
    pythonprint(*word,sep=sep,end="",file=file,flush=flush)
    pythonprint(f'\033'+"[0m",end=end)
