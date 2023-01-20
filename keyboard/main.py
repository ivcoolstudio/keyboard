import pyautogui as root
from time import sleep

txt = input("text")

sleep(5)#bot activation time

root.typewrite( txt, 0.3 ) #the speed of writing text