#Este codigo crea un archivo python y lo comprime en la carpeta Escritorio, despues ingresa al correo gmail y envia un correo con asunto.

import pyautogui as py
import time
import pyperclip

py.FAILSAFE = False

py.hotkey('win', 'r')

time.sleep(1)

# py.typewrite('cmd')

py.press('enter')

time.sleep(1)

py.typewrite('cd desktop\n')

time.sleep(1)

py.typewrite("mkdir hello-world\n")

time.sleep(1)

py.typewrite('cd hello-world\n')

time.sleep(1)

py.typewrite('COPY CON app.py\n')

py.typewrite('nombre = "Dayismar Rodriguez"\n')

py.typewrite('skills = "Dayismar Rodriguez"\n')

py.typewrite('experienciaEnProgramacion = "Dayismar Rodriguez"\n')

py.typewrite('edad = "Dayismar Rodriguez"\n')

py.typewrite('''print('Soy ' ''')

pyperclip.copy('+')

py.hotkey('ctrl', 'v')

py.typewrite(''' nombre ''')

py.hotkey('ctrl', 'v')

py.typewrite(''' ' tengo hablidad con ' ''')

py.hotkey('ctrl', 'v')

py.typewrite(''' skills ''')

py.hotkey('ctrl', 'v')

py.typewrite(''' ' mi experiencia en programacion consiste en ' ''')

py.hotkey('ctrl', 'v')

py.typewrite('''experienciaEnProgramacion''')

py.hotkey('ctrl', 'v')

py.typewrite(''' ' y mi edad es' ''')

py.hotkey('ctrl', 'v')

py.typewrite('''edad)\n''')

py.hotkey('ctrl', 'c')

py.typewrite('cd..\n')

time.sleep(1)

py.typewrite('rar a -r -rr "helloWorld2.rar" "hello-world"\n')

time.sleep(1)

py.typewrite('start chrome https://mail.google.com/mail/u/0/?tab=rm"&"ogbl#inbox\n')

time.sleep(3)

redactarBtnPoint = py.locateCenterOnScreen('img/redactar.png')

time.sleep(1)

redactarBtnPointX = redactarBtnPoint.x

redactarBtnPointY = redactarBtnPoint.y

py.click(redactarBtnPointX, redactarBtnPointY)

time.sleep(1)

py.typewrite('rdayismar')

pyperclip.copy('@')

py.hotkey('ctrl', 'v')

py.typewrite('gmail.com\n')

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

escritorio = py.locateCenterOnScreen('img/escritorio.png')

escritorioHover = py.locateCenterOnScreen('img/escritorio-hover.png')

if escritorio:
    escritorioX = escritorio.x
    escritorioY = escritorio.y
    py.click(escritorioX, escritorioY)
else:
    escritorioHoverX = escritorioHover.x
    escritorioHoverY = escritorioHover.y
    py.click(escritorioHoverX, escritorioHoverY)

time.sleep(1)

buscar = py.locateCenterOnScreen('img/buscar.png')

buscarHover = py.locateCenterOnScreen('img/buscar-hover.png')

if buscar:
    buscarX = buscar.x
    buscarY = buscar.y
    py.click(buscarX, buscarY)
    py.typewrite('helloWorld2.rar\n')
else:
    py.typewrite('helloWorld2.rar\n')

time.sleep(2)

Enviar = py.locateCenterOnScreen('img/Enviar.png')

EnviarX = Enviar.x

EnviarY = Enviar.y

py.click(EnviarX, EnviarY)
