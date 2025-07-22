import os
from time import sleep

emptycmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\drainingthem.txt'

while True:
    sleep(300)
    with open(emptycmd, 'r') as file:
        lines = file.readlines()

        print(lines)
        print('Deleting all lines')

        with open(emptycmd, "w") as f:
            pass  # Do nothing, but opening the file in "w" mode clears its content