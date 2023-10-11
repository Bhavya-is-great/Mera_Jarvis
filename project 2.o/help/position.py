import pyautogui
from time import sleep

sleep(8)
position = pyautogui.position()
print(position)
pyautogui.click(x=539, y=439)