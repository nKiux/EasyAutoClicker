import os
try:
    import mouse
    import time
    import pynput.keyboard
    import threading
except:
    os.system('pip install pynput')
    os.system('pip install mouse')
    os.system('pip install pyqt5')

import mouse
import time
import pynput.keyboard
import threading

t = 0.5
R_start = False
L_start = False


def RClick():
     while R_start:
          mouse.click('right')
          time.sleep(0.5)

def LClick():
     while L_start:
          mouse.click('left')
          time.sleep(0.5)

def on_press(k):
    global R_start, L_start
    if k == pynput.keyboard.Key.page_up:
        print('Left Triggered!')
        if L_start == False:
            L_start = True
            threading.Thread(target=LClick).start()
            
        else:
            L_start = False
        print(L_start)

    if k == pynput.keyboard.Key.page_down:
        print('Right Triggered!')
        if R_start == False:
            R_start = True
            threading.Thread(target=RClick).start()
        else:
            R_start = False
        print(R_start)
            

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

