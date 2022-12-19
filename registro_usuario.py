from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def registrarse():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()


def botonCrear():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def login():
    if requirement in labelObtained:
        print("Estado: Pass")
        print("FIN DEL CASO DE PRUEBA")
        print()
    else:
        print("Estado: Fail")
        print("FIN DEL CASO DE PRUEBA")
        print()

# Seleccionamos el driver de chrome para realizar la prueba
driver = webdriver.Chrome()

# Maximizamos la pantalla para realizar la prueba
driver.maximize_window()

# 1-Acceder al link https://www.arredo.com.ar/login
driver.get("https://www.arredo.com.ar/login")
time.sleep(2)

# 2-Clickear en la opción "ENTRAR CON E-MAIL Y CONTRASEÑA"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/ul/li[2]/div/button/div').click()
time.sleep(2)

# 3-Validar que se visualice la opción para crear una cuenta
requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[5]/a')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[5]/a').text

labelObtained = labelComprarButton

print()
print('Se visualiza un link para crear una cuenta:', labelObtained)

requirement = '¿No tiene una cuenta? Regístrese'

registrarse()

# 4-Clickear en la opción "¿No tiene una cuenta? Regístrese"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[5]/a').click()
time.sleep(2)

# 5-Clickear en la opción para ingresar el mail
usuario = driver.find_element(By.NAME, 'email')
time.sleep(2)

# 6-Ingresar el correo electronico en el campo "email"
usuario.send_keys("fruxafrauquoppe-8760@yopmail.com")

# 7-Clickear en el botón "ENVIAR" debajo del formulario del correo electrónico
usuario.send_keys(Keys.ENTER)
time.sleep(7)

# 8-Ingresar el código enviado al mail anteriormente ingresado
# PASO MANUAL

# 9-Ingresar la contraseña en el campo "Ingrese su contraseña"
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[2]/div/label/div/input')
password.send_keys('123456789Ma')
time.sleep(2)

# 10-Ingresar nuevamente la contraseña en el campo "Confirmar contraseña"
confirmar_password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[3]/label/div/input')
confirmar_password.send_keys('123456789Ma')
time.sleep(30)

# 11-Validar que se visaulice el boton para crear una cuenta
requirement = ()     #Validar que se visualiza el boton para crear una cuenta
labelObtained = ()      #Se visualiza el boton para crear una cuenta

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[4]/div[2]/button/div/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[4]/div[2]/button/div/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza el boton para crear una nueva cuenta:', labelObtained)


requirement = 'CREAR'

botonCrear()

# 12- Clickear en la opción "CREAR" ubicado abajo del campo "Confirmar contraseña"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[4]/div[2]/button').click()
time.sleep(30)

# 13-Clickear en la opcion para cerrar el POP UP
driver.find_element(By.XPATH, '//*[@id="btnNoIdWpnPush"]').click()
time.sleep(5)

# 14- Validar que el usuario es redirigido a la home de la pagina web
requirement = ()     #Validar que se visualice un mensaje con el siguiente formato "hola" + nombre_del_usuario
labelObtained = ()      #Se visualoza el mensaje de bienvenida con el formato "hola" + "nombre_del_usuario"

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button/div/span/div/div/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button/div/span/div/div/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza un mensaje de bienvenida con el siguiente Formato:', labelObtained)

requirement = 'Hola'

login()

driver.close()