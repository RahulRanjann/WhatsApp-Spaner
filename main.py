import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
msssges = "Hi i am a python bot crated by rahul. I send you 50 messags. i am so sorry"
#Hi i am a python bot crated by rahul. I send you 50 messags. i am so sorry

pyautogui.click(1528, 991)
pyautogui.write(msssges, interval=0.1)
time.sleep(9)
pyautogui.press('enter')
i = 1
for _ in  range(25):
    
    pyautogui.click(1528, 991)
    pyautogui.write(f'massage_no.{i}')
    time.sleep(1)
    pyautogui.press("enter")
    i += 1