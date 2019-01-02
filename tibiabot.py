#####################################
#####################################
#TO WSZYSTKO NA DOLE JEST DLA FULLHD#
#####################################
#####################################

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, ReleaseKey


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # edge detection
    #processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def health_green():
    #wartosci ponizej to tak +- 90% hp
    #trzeba pamietac o przedziale ###anytbot
    px=ImageGrab.grab().load()
    for y in range(28,29,1):# <- koordynaty od 20,30 dla y
        for x in range(720,780,10):# <- koordynaty od 720 do 780 dla x
                color=px[x,y]
    ## 38,39,39 - pixele sa ciemne - nie ma tyle hp
    ## 0,137,0 - pixele sa zielone - jest hp
    if color[0] == 38 and color[0] != 0 and color[1] == 39 and color[1] != 137 and color[2] == 39 and color[2] != 0:
        return True
    else:
        return False

def health_yellow():
    px=ImageGrab.grab().load()
    for y in range(28,29,1):# <- koordynaty od 20,30 dla y :: ZOSTAJE NA ZAWSZE TAKIE SAMO
        for x in range(590,600,1):# <- koordynaty od 720 do 780 dla x :: Tu zmeniamy wlasnie od ilosci zycia
                color=px[x,y]
    ## 38,39,39 - pixele sa ciemne - nie ma tyle hp
    if color[0] == 45 and color[1] == 45 and color[2] == 45:
        return True
    else:
        return False

def health_black():
    px=ImageGrab.grab().load()
    for y in range(35,36,1):# <- koordynaty od 20,30 dla y :: ZOSTAJE NA ZAWSZE TAKIE SAMO
        for x in range(17,18,11):# <- koordynaty od 720 do 780 dla x :: Tu zmeniamy wlasnie od ilosci zycia
                color=px[x,y]
    ## 38,39,39 - pixele sa ciemne - nie ma tyle hp
    if color[0] == 175 and color[1] == 44 and color[2] == 44:
        return True
    else:
        return False


def healing():
    if health_black():
        print("POWOLI UMIERAM, NACISKAM F3 - EXURA VITA")
        pyautogui.keyDown('f3')
        #PressKey(0x70) naciska wszyskto tylko nie "efy"...
        #ReleaseKey(0x70)
        pyautogui.keyUp('f3')
        time.sleep(0.2)

    if health_yellow():
        print("JEST ZLE, NACISKAM F2 - EXURA GRAN")
        pyautogui.keyDown('f2')
        #PressKey(0x70) naciska wszyskto tylko nie "efy"...
        #ReleaseKey(0x70)
        pyautogui.keyUp('f2')
        time.sleep(0.2)

    if health_green():
        print("NACISKAM F1 - EXURA")
        pyautogui.keyDown('f1')
        #PressKey(0x70) naciska wszyskto tylko nie "efy"...
        #ReleaseKey(0x70)
        pyautogui.keyUp('f1')
        time.sleep(0.2)

def processing(last_time):
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    print('Frame took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    new_screen = process_img(screen)

def main():
    while True:
        #PressKey(W)
        last_time = time.time()
        processing(last_time)
        print("Health green:")
        print(health_green())
        print("Health yellow:")
        print(health_yellow())
        print("Health black:")
        print(health_black())
        healing()






        #cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        #if cv2.waitKey(25) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()
        #    break

main()
