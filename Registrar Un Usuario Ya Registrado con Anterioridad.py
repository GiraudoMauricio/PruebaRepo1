from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""Seleccionamos el driver de chrome para realizar la prueba"""
driver = webdriver.Chrome()

"""Maximizamos la pantalla para realizar la prueba"""
driver.maximize_window()

# 1-Acceder al link https://www.arredo.com.ar/login
driver.get("https://www.arredo.com.ar/login")
time.sleep(2)

# 2-Clickear en la opción "ENTRAR CON E-MAIL Y CONTRASEÑA"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/ul/li[2]/div/button/div').click()
time.sleep(2)

# 3-Validar que se visualice la opción para crear una cuenta

# 4-Clickear en la opción "¿No tiene una cuenta? Regístrese"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[5]/a').click()
time.sleep(2)

# 5-Clickear en la opción para ingresar el mail
usuario = driver.find_element(By.NAME, 'email')
time.sleep(2)

# 6-Ingresar el correo electronico en el campo "email"
usuario.send_keys("fruxafrauquoppe-8760@yopmail.com")

# 7-Clickear en la botón "ENVIAR" debajo del formulario del correo electrónico
usuario.send_keys(Keys.ENTER)
time.sleep(7)

# 8-Validar un mensaje de error en la pantalla.
