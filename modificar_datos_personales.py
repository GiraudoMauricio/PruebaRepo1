from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Seleccionamos el driver de chrome para realizar la prueba
driver = webdriver.Chrome()

# Maximizamos la pantalla para realizar la prueba
driver.maximize_window()

# 1-Acceder al link
driver.get("https://www.arredo.com.ar")
time.sleep(2)

# 2-Clickear en la opción para iniciar sesión ubicado en la parte superior derecha de la pagina web.
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button').click()
time.sleep(8)

# 3-Clickear en la opción "Recibir código de acceso por e-mail".
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/button/div').click()
time.sleep(2)

# 4-Ingresar el correo electrónico en el campo "email" 
email = driver.find_element(By.NAME, 'email')
email.send_keys('fruxafrauquoppe-8760@yopmail.com')

# 5-Clickear en la opcion "ENVIAR" ubicado abajo del campo "email" 
email.send_keys(Keys.ENTER)
time.sleep(15)

# 6-Ingresar el código enviado al correo electrónico ingresado en el campo "token"
#                   ------------ PASO MANUAL ------------


# 7-Clickear en el botón "CONFIRMAR" para enviar el código de validación. 
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span').click()
time.sleep(10)


# 8-Validar que el token ingresado coincida con el token que fue enviado por mail 
verificacion_login = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button/div/span/div/div')
assert verificacion_login.text == "Holaaa"


# 9-Clickear en la opcion para cerrar el POP UP
driver.find_element(By.XPATH, '//*[@id="btnNoIdWpnPush"]').click()
time.sleep(5)

# 10-Validar que el usuario ingreso al home a través de su cuenta

# 11-Clickear en la opcion para acceder al perfil
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button').click()
time.sleep(5)

#  12-Clicker en la opcion 'Mi cuenta'
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a/button/span').click()
time.sleep(8)


#  13-Validar que se visualiza el botón para editar la información personal


#  14-Clickear en la opcion para editar los datos personales
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button').click()
time.sleep(5)

#  15-Clickear en el campo "Nombre" e ingresar el nombre del usuario
nombre = driver.find_element(By.NAME, 'firstName')
nombre.send_keys('Agente')
time.sleep(5)

#  16-Clickear en el campo "Apellido" e ingresar el apellido del usuario
apellido = driver.find_element(By.NAME, 'lastName')
apellido.send_keys('007')
time.sleep(5)

#  17-Clickear en el campo "DNI" e ingresar un numero de documento
documento = driver.find_element(By.NAME, 'document')
documento.send_keys('85456321')
time.sleep(5)


#  18-Validar que el número de documento tenga solo 8 caracteres y este solo conformado por números


#  19-Clickear en el botón 'Guardar cambios' """
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/button/div').click()
time.sleep(5)

#  20-Clickear sobre el logo de arredo ubicado en la parte superior de la pagina.
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a').click()
time.sleep(15)

#  21- Validar que el usuario volvió al home
