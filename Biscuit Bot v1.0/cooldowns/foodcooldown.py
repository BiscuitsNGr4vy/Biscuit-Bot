import os
from time import sleep

foodcmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\feedingthem.txt'

while True:
    sleep(300)
    with open(foodcmd, 'r') as file:
        lines = file.readlines()

        print(lines)
        print('Deleting all lines')

        with open(foodcmd, "w") as f:
            pass  # Do nothing, but opening the file in "w" mode clears its content