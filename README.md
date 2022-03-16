# colorprint3
A simple library to print with color and style on Python 3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install colorprint3.

```bash
pip install colorprint3
```

## Usage
Same as build-in ```print()``` function but have a few extra arguments : ```fg_color```, ```bg_color``` and ```style```.

```python
colorprint3.print(*word,sep=None,end=None,file=None,flush=True,fg_color=None,bg_color=None,style=[])
```
```fg_color``` values : ```black```, ```red```, ```green```, ```yellow```, ```blue```, ```magenta```, ```cyan```, ```white```, ```s_black```, ```s_red```, ```s_green```, ```s_yellow```, ```s_blue```, ```s_magenta```, ```s_cyan```, ```s_white``` & Custom colors.

```bg_color``` values : ```black```, ```red```, ```green```, ```yellow```, ```blue```, ```magenta```, ```cyan```, ```white```, ```s_black```, ```s_red```, ```s_green```, ```s_yellow```, ```s_blue```, ```s_magenta```, ```s_cyan```, ```s_white``` & Custom colors.

```style``` values : ```bold```, ```underline```, ```italic```, ```faint```. Accepting multiple style by putting them inside a list.

Custom color format : ```[r,g,b]```
## Contributing
Please open an issue to report a bug or give suggestion. Feel free to fork this project.

## License
[GNU GPLv3+](https://choosealicense.com/licenses/gpl-3.0/)
