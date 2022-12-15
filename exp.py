import pyautogui
import time as t
from PIL import ImageGrab
import random

def rnd(n,m):
    return random.randint(n,m)


t.sleep(1)
xy_pos = (451, 388)
x1 = xy_pos[0]-2
x2 = xy_pos[0]+2
y1 = xy_pos[1]-2
y2 = xy_pos[1]+2

##################
xypos2 = (773, 538)
x11 = xypos2[0]-1
x22 = xypos2[0]+1
y11 = xypos2[1]-1
y22 = xypos2[1]+1


while(True):
    
    igmr = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    igmr2 = ImageGrab.grab(bbox=(x11,y11,x22,y22))
    pxl = igmr.load()
    pxl2 = igmr2.load()

    if(pxl[1,0][0] > 160): #opekom appears
        t.sleep(random.uniform(0.8, 1.1))
        if(pxl2[1,0] == (81, 81, 81)): #healing

            pyautogui.press('1') 
            t.sleep(random.uniform(0.1, 0.3))
            pyautogui.press('4') 

            t.sleep(1.5) #text


        else: #attack

            pyautogui.press('1') 
            t.sleep(random.uniform(0.1, 0.3))
            pyautogui.press('1') 


            t.sleep(1.5) #text
            
    else: #move
        pyautogui.keyDown('a')
        t.sleep(random.uniform(0.75, 1.2))
        pyautogui.keyUp('a')
        t.sleep(random.uniform(0.2, 0.5))
        pyautogui.keyDown('d')
        t.sleep(random.uniform(0.75, 1.2))
        pyautogui.keyUp('d')
    
