import pyautogui as py

import time

py.FAILSAFE = False

py.hotkey('win', 'r')

# py.typewrite('cmd')

py.press('enter')

py.typewrite('cd desktop\n')

py.typewrite("mkdir hello-world\n")

py.typewrite('cd hello-world\n')

py.typewrite('COPY CON app.py\n')

py.typewrite('nombre = "Dayismar Rodriguez"\n')

py.typewrite('skills = "Dayismar Rodriguez"\n')

py.typewrite('experienciaEnProgramacion = "Dayismar Rodriguez"\n')

py.typewrite('edad = "Dayismar Rodriguez"\n')

py.hotkey('ctrl', 'c')

py.typewrite('cd..\n')

py.typewrite('rar a -r -rr "helloWorld2.rar" "hello-world"\n')

py.typewrite('start chrome https://mail.google.com/mail/u/0/?tab=rm"&"ogbl#inbox\n')

time.sleep(2)

redactarBtnPoint = py.locateCenterOnScreen('img/redactar-btn.png')

redactarBtnPointX = redactarBtnPoint.x

redactarBtnPointY = redactarBtnPoint.y

py.click(redactarBtnPointX, redactarBtnPointY)

time.sleep(2)

py.typewrite('rdayis')

time.sleep(1)

py.hotkey('alt', '6', '4')

py.typewrite('gmail.com')

time.sleep(2)


# email = py.locateCenterOnScreen('img/dayisMail.png')

# emailX = email.x

# emailY = email.y

# py.click(emailX, emailY)

time.sleep(2)

asunto = py.locateCenterOnScreen('img/asunto.png')

asuntoX = asunto.x

asuntoY = asunto.y

py.click(asuntoX, asuntoY)

py.typewrite('Test de Prueba', interval=.2)

py.press('tab')

py.typewrite('Correo de prueba')

adjuntar = py.locateCenterOnScreen('img/adjuntar.png')

adjuntarX = adjuntar.x

adjuntarY = adjuntar.y

py.click(adjuntarX, adjuntarY)

time.sleep(2)

escritorio = py.locateCenterOnScreen('img/escritorio.png')

escritorioX = escritorio.x

escritorioY = escritorio.y

py.click(escritorioX, escritorioY)

time.sleep(2)

barraDeTexto = py.locateCenterOnScreen('img/barraDeTexto.png')

barraDeTextoX = barraDeTexto.x

barraDeTextoY = barraDeTexto.y

py.click(barraDeTextoX, barraDeTextoY)

py.typewrite('helloWorld2.rar\n')

time.sleep(2)

Enviar = py.locateCenterOnScreen('img/Enviar.png')

EnviarX = Enviar.x

EnviarY = Enviar.y

py.click(EnviarX, EnviarY)
