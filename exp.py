import pyautogui
import time as t
from PIL import ImageGrab


t.sleep(1)
xy_pos = (684, 387)
x1 = xy_pos[0]-2
x2 = xy_pos[0]+2
y1 = xy_pos[1]-2
y2 = xy_pos[1]+2

while(True):
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    pxl = igmr.load()
    print(pxl[0,0][0])
    if(pxl[0,0][0] > 160): #opekom appears
        pyautogui.press('1') 

    else:
        pyautogui.keyDown('a')
        t.sleep(0.75)
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        t.sleep(0.75)
        pyautogui.keyUp('d')
