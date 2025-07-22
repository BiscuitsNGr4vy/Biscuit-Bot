import pyautogui
from time import sleep

mess = "Server Restarting in 10min"
mess2 = "Server Restarting in 5min"
mess3 = "Server Restarting in 3min"
mess4 = "Server Restarting in 1min"
mess5 = "Server Restarting in 30sec"
mess6 = "Server Restarting"

sleep(21000)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e) 

sleep(299)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess2))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e) 

sleep(119)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess3))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e)

sleep(119)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess4))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e) 

sleep(29)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess5))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e) 

sleep(26)
try:
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess6))
        pyautogui.click(1737, 380, duration=0.2) 
    
except Exception as e:
        print(e) 