import pyautogui
import time as t
from PIL import ImageGrab
import random

def attack():
    print("a")
    t.sleep(1)
    pyautogui.press('1') #attack
    t.sleep(random.uniform(0.3, 0.4))
    pyautogui.press('1') #heal

def heal():
    print("h")
    t.sleep(1)
    pyautogui.press('1') #attack
    t.sleep(random.uniform(0.3, 0.4))
    pyautogui.press('4') #heal

def percent(x1,y1,x2,y2):
    hp_bar = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    im = hp_bar.load()
    
    r=0 #amount of red
    b=0 #amount of black

    for x in range(x2-x1):
        for y in range(y2-y1):
            if(im[x,y][0] == im[x,y][1] and im[x,y][0] != (255,255,255)): #colour filter
                im[x,y] = (0,0,0)
                b = b +1
            else:
                im[x,y] = (255,0,0)
                r = r +1
    
    hp_bar.save("test.png")
    print(r,b)
    return (r)/(r+b) #percent




t.sleep(1)
xypos = [(679, 380), (854, 381)] #enemy pokemon hp  | x1,y1,x2,y2
xypos2 = [(1096, 599),(1272, 600)] #hp of own pokemon
xypos3 = ()

while(True):
    
    im = ImageGrab.grab()
    pxl = im.load()
    print(pxl[xypos[0]])
    if(pxl[xypos[0]][0] > 240): #pokemon present
        t.sleep(1.5)
        #heal/attack logic
        if(percent(xypos2[0][0], xypos2[0][1],xypos2[1][0], xypos2[1][1]) < 0.6): #heal when pokemon drops under 60% hp
            heal()
            pass

        else: #attack
            attack()

        t.sleep(2)
        if(percent(xypos[0][0], xypos[0][1],xypos[1][0], xypos[1][1]) != 0):
            #pokemon still alive attack if hp is sufficient | over 40% hp threshold
            if(percent(xypos2[0][0], xypos2[0][1],xypos2[1][0], xypos2[1][1]) > 0.4):
                t.sleep(2.5)
                attack() #killing blow
            else:
                heal()
                t.sleep(2.5)
                attack()

        else:
            #pokemon dead
            pass
    else:
        print("m")
        t.sleep(0.2)
        pyautogui.keyDown('a')
        t.sleep(random.uniform(0.75, 1.2))
        pyautogui.keyUp('a')
        t.sleep(random.uniform(0.2, 0.5))
        pyautogui.keyDown('d')
        t.sleep(random.uniform(0.75, 1.2))
        pyautogui.keyUp('d')


