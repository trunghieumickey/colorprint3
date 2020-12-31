# colorprint3
A simple library to print color on Python 3

Build Status : 
![Python Package](https://github.com/trunghieumickey/colorprint3/workflows/Python%20package/badge.svg?branch=master)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install colorprint3.

```bash
pip install colorprint3
```

## Usage
Same as build-in ```print()``` function but have 2 more input ```fg_color``` and ```bg_color```.

```python
colorprint3.print(*word,sep=None,end=None,file=None,flush=True,fg_color=None,bg_color=None)
```
Avalable Colors : ```black```, ```red```, ```green```, ```yellow```, ```blue```, ```magenta```, ```cyan```, ```white```, ```s_black```, ```s_red```, ```s_green```, ```s_yellow```, ```s_blue```, ```s_magenta```, ```s_cyan```, ```s_white```.

## Contributing
Please open an issue to report a bug or give suggestion. Feel free to fork this project.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
