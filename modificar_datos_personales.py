from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""Seleccionamos el driver de chrome para realizar la prueba"""
driver = webdriver.Chrome()

"""Maximizamos la pantalla para realizar la prueba"""
driver.maximize_window()

"""Ingresar a la web"""
driver.get("https://www.arredo.com.ar")
time.sleep(2)

"""Clickear en la opcion para iniciar sesion"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button').click()
time.sleep(8)

"""Clickear en la opcion 'Recibir código de acceso por e-mail'"""
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/button/div').click()
time.sleep(2)

"""Igresar el correo electronico en el input"""
email = driver.find_element(By.NAME, 'email')
email.send_keys('fruxafrauquoppe-8760@yopmail.com')
email.send_keys(Keys.ENTER)
time.sleep(15)

# """Clickear en la opcion 'ENVIAR' """
# driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span').click()
# time.sleep(18)

"""Clickear en la opcion 'CONFIRMAR' """
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button/div/span').click()
time.sleep(10)

"""Clickear en la opcion para cerrar el POP UP"""
driver.find_element(By.XPATH, '//*[@id="btnNoIdWpnPush"]').click()
time.sleep(5)

"""Clickear en la opcion para acceder al perfil"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button').click()
time.sleep(5)

"""Clicker en la opcion 'Mi cuenta'"""
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a/button/span').click()
time.sleep(8)

"""Clickear en la opcion para editar los datos personales"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button').click()
time.sleep(5)

"""Clickear en la opcion para ingresar el nombre de usuario"""
nombre = driver.find_element(By.NAME, 'firstName')
nombre.send_keys('Agente')
time.sleep(5)

"""Clickear en la opcion para ingresar Apellido"""
apellido = driver.find_element(By.NAME, 'lastName')
apellido.send_keys('007')
time.sleep(5)

"""Clickear en la opcion para ingresar el documento"""
documento = driver.find_element(By.NAME, 'document')
documento.send_keys('85456321')
time.sleep(5)

"""Clickear en la opcion para guardar la informacion personal"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/button/div').click()
time.sleep(5)

"""Clickear en el logo de la pagina ubicado en la parte superior de la pantalla para volver al home de la pagina web"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a').click()
time.sleep(15)