import pyautogui as py 

im1 = py.screenshot('img/screen.png')

redactarBtn = py.locateCenterOnScreen('img/redactar-btn.png')

redactarBtnX = redactarBtn.x

redactarBtnY = redactarBtn.y

py.click(redactarBtnX, redactarBtnY)

print(redactarBtn)
int