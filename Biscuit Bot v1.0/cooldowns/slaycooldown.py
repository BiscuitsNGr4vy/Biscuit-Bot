import os
from time import sleep

slaycmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\queuedcoms.txt'

while True:
    sleep(900)
    with open(slaycmd, 'r') as file:
        lines = file.readlines()

        print(lines)
        print('Deleting all lines')

        with open(slaycmd, "w") as f:
            pass  # Do nothing, but opening the file in "w" mode clears its content