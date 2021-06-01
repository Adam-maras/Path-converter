# Foobar

Some programing languages cant read paths that uses \ to separate folder, this code is the solution, it can take a normal path and transform it in to a readable. And it will add it to the clipboard. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
For windows users:
    import pyperclip (install it with pip)
For mac-os users:
    import subprocess

```

## Usage

```python
import pyperclip


print('I will transform your \ in /')
str = input('Enter the string that you want me to modify: ')
converted_str = str.replace("\\", "/")

pyperclip.copy(converted_str)
spam = pyperclip.paste()
print('we have added: ' + converted_str + ' to the clipboard')

"""
FOR MAC-OS USERS!
Remove line 9 and 10 and replace it with: 
    subprocess.run("pbcopy", universal_newlines=True, input=data")

Dont forget write "import subprocess" at the beginnings of your code
"""
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
