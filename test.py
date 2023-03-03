import pyautogui as py 
import time

py.hotkey('win', 'q')

py.typewrite('cmd')

time.sleep(1)

cmd = py.locateCenterOnScreen('img\cmd.png')

print(cmd)

# cmdx = cmd.x

# cmdy = cmd.y

# time.sleep(2)

# py.click(cmdx, cmdy)