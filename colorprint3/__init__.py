from builtins import print as pythonprint
def print(*word, sep=None, end=None, file=None, flush=None, fg_color=None, bg_color=None, style=[]):
    style_dic = {
        "black": 0, "red": 1, "green": 2, "yellow": 3, "blue": 4, "magenta": 5, "cyan": 6, "white": 7,
        "bold": 1, "faint": 2, "italic": 3, "underline": 4
    }
    formatlist = []
    clor = [fg_color, bg_color]
    for i in range(len(clor)):
        if not clor[i]:
            continue
        if type(clor[i]) == type([]):
            if len(clor[i]) == 3:
                formatlist.append(38+i*10)
                formatlist.append(2)
                formatlist.extend(clor[i])
        else:
            if (type(clor[i]) == type("")):
                clor[i] = clor[i].split('_')
                clor[i] = style_dic[clor[i][-1]]+(clor[i][0] == 's')*60
            formatlist.append(30+clor[i]+i*10)
    if type(style) != type([]):
        style = [style]
    for i in style:
        if i in style_dic:
            formatlist.append(style_dic[i])
    pythonprint(f'\033[', end="")
    pythonprint(*formatlist, sep=";", end="m")
    pythonprint(*word, sep=sep, end="", file=file, flush=flush)
    pythonprint(f'\033'+"[0m", end=end)
