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
