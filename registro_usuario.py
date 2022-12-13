from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""Seleccionamos el driver de chrome para realizar la prueba"""
driver = webdriver.Chrome()

"""Maximizamos la pantalla para realizar la prueba"""
driver.maximize_window()

"""Ingresar a la web"""
driver.get("https://www.arredo.com.ar/login")
time.sleep(2)

"""Clickear en la opcion 'ENTRAR CON E-MAIL Y CONTRASEÑA'"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/ul/li[2]/div/button/div').click()
time.sleep(2)

"""Clickear en la opcion '¿No tiene una cuenta? Regístrese'"""
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[5]/a').click()
time.sleep(2)

"""Clickear en la opcion para ingresar el mail"""
usuario = driver.find_element(By.NAME, 'email')
time.sleep(2)

"""Ingresar el correo electronico"""
usuario.send_keys("fruxafrauquoppe-8760@yopmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(7)

"""Ingresar la contrasela"""
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[2]/div/label/div/input')
password.send_keys('123456789Ma')
time.sleep(2)

"""Ingresar nuevamente la contraseña"""
confirmar_password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/form/div[3]/label/div/input')
confirmar_password.send_keys('123456789Ma')
time.sleep(30)