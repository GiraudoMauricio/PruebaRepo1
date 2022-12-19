from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def login():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def opcionLogin():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def botonEnviar():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def opcionMiCuenta():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def botonEditarInformacion():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def botonGuardarCambios():
    if requirement in labelObtained:
        print("Estado: Pass")
        print()
    else:
        print("Estado: Fail")
        print()

def volverAlHome():
    if requirement in labelObtained:
        print("Estado: Pass")
        print('FIN DEL CASO DE PRUEBA')
        print()
    else:
        print("Estado: Fail")
        print()


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

# 3-Validar que se visualice la opcion para iniciar sesion mediante codigo enviado por mail
requirement = ()     #Se visualiza una opcion para inciar sesion mediante un codigo enviado por mail
labelObtained = ()      #Se visualiza la opcion para inciar sesion mediante un codigo enviado por mail

comprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/button/div/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/button/div/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza la opcion:', labelObtained)

requirement = 'RECIBIR CÓDIGO DE ACCESO POR E-MAIL'

opcionLogin()

# 4-Clickear en la opción "Recibir código de acceso por e-mail".
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/button/div').click()
time.sleep(2)

# 5-Ingresar el correo electrónico en el campo "email" 
email = driver.find_element(By.NAME, 'email')
email.send_keys('fruxafrauquoppe-8760@yopmail.com')

# 6-Validar que se visualice el boton para enviar el codigo al correo electronico
requirement = ()     #Se visualiza la opcion para enviar el codigo al mail
labelObtained = ()      #El usuario visualiza la opcion para enviar el codigo de acceso al correo que ingreso

comprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza la opcion:', labelObtained)

requirement = 'ENVIAR'

botonEnviar()


# 7-Clickear en la opcion "ENVIAR" ubicado abajo del campo "email" 
email.send_keys(Keys.ENTER)
time.sleep(25)


# 8-Ingresar el código enviado al correo electrónico ingresado en el campo "token"
#                   ------------ PASO MANUAL ------------


# 9-Clickear en el botón "CONFIRMAR" para enviar el código de validación. 
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span').click()
time.sleep(15)


# 10-Clickear en la opcion para cerrar el POP UP
driver.find_element(By.XPATH, '//*[@id="btnNoIdWpnPush"]').click()
time.sleep(10)

# 11-Validar que el usuario ingreso al home a través de su cuenta
requirement = ()     #Se visualiza un mensaje con el siguiente formato "hola" + nombre_del_usuario
labelObtained = ()      #Se visualiza el mensaje de bienvenida con el formato "hola" + "nombre_del_usuario"

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button/div/span/div/div/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button/div/span/div/div/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza un mensaje de bienvenida con el siguiente Formato:', labelObtained)

requirement = 'Hola'

login()


# 12-Clickear en la opcion para acceder al perfil
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button').click()
time.sleep(5)


# 13-Validar que se visualice la opcion para ingresar a mi cuenta
requirement = ()     #Se visualiza la opcion para ingresar a la cuenta del usuario.
labelObtained = ()      #El usuario visualiza una opcion para ingresar a la informacion de su cuenta.

comprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a/button/span')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a/button/span').text

labelObtained = labelComprarButton

print()
print('Se visualiza la opcion:', labelObtained)

requirement = 'MI CUENTA'

opcionMiCuenta()

#  14-Clickear en la opcion 'Mi cuenta'
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a/button/span').click()
time.sleep(35)


#  15-Validar que se visualice el botón para editar la información personal
requirement = ()     #Se visualiza un boton para editar la informacion personal.
labelObtained = ()      #El usuario visualiza el boton para editar la informacion personal.

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button/div')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button/div').text

labelObtained = labelComprarButton

print()
print('Se visualiza la opcion: ', labelObtained)

requirement = 'Editar'

botonEditarInformacion()


#  16-Clickear en la opcion para editar los datos personales
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button').click()
time.sleep(5)


#  17-Clickear en el campo "Nombre" e ingresar el nombre del usuario
nombre = driver.find_element(By.NAME, 'firstName')

# Para elimiar el contenido de los campos implemete el .clear pero no dio resultados,
# por lo tanto implemente un ciclo for de la forma mas clara posible.
for i in range(6):
    nombre.send_keys(Keys.BACK_SPACE)

time.sleep(2)
nombre.send_keys('Agente')
time.sleep(5)


#  18-Clickear en el campo "Apellido" e ingresar el apellido del usuario
apellido = driver.find_element(By.NAME, 'lastName')

for i in range(4):
    apellido.send_keys(Keys.BACK_SPACE)

time.sleep(2)
apellido.send_keys('007')
time.sleep(5)


#  19-Clickear en el campo "DNI" e ingresar un numero de documento
documento = driver.find_element(By.NAME, 'document')

for i in range(9):
    documento.send_keys(Keys.BACK_SPACE)

time.sleep(2)
documento.send_keys('85456321')
time.sleep(5)


# 20-Validar que se visualice el boton para guardar los cambios del perfil
requirement = ()     #Se visualiza un boton para guardar los cambios
labelObtained = ()      #El usuario visualiza el boton para guardar los cambios realizados en su perfil.

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/button/div')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/button/div').text

labelObtained = labelComprarButton

print()
print('Validar que se visualiza el boton: ', labelObtained)

requirement = 'Guardar cambios'

botonGuardarCambios()

#  21-Clickear en el botón 'Guardar cambios'
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/button/div').click()
time.sleep(5)


#  22-Clickear sobre el logo de arredo ubicado en la parte superior de la pagina.
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a').click()
time.sleep(15)


# 23- Validar que el usuario volvió al home
requirement = ()     #El usuario vuelve al home de la pagina web y visualiza las opciones del home
labelObtained = ()      #El usuario visualiza las opciones del home

comprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[1]/div/a/div')

labelComprarButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[1]/div/a/div').text

labelObtained = labelComprarButton

print()
print('Una de las opciones disponibles luego de volver al home es: ', labelObtained)

requirement = 'ROPA DE CAMA'

volverAlHome()

driver.close()