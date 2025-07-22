import os
from time import sleep

chatcmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\usercommands.txt'

while True:
    sleep(900)
    with open(chatcmd, 'r') as file:
        lines = file.readlines()

        print(lines)
        print('Deleting all lines')

        with open(chatcmd, "w") as f:
            pass  # Do nothing, but opening the file in "w" mode clears its content