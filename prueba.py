from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login/identify/?ctx=recover%27")

number = driver.find_element_by_xpath('//*[@id="identify_email"]')

time.sleep(5)

number.send_keys("+777558493")

did_submit = driver.find_element_by_name('did_submit')

did_submit.click()

time.sleep(3)

submit = driver.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[2]/div/div[1]/button')

submit.click()

time.sleep(3)