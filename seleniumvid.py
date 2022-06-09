import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://wwww.olx.com.ec/autos_c378')

# todos los anuncios en una lista
autos = driver.find_elements(by=By.XPATH, value='//li[@data-aut-id="itemBox"]')

boton = driver.find_element(by=By.XPATH, value='//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    boton.click()
    sleep(random.uniform(3.0, 5.0))
    boton = driver.find_element(by=By.XPATH, value='//button[@data-aut-id="btnLoadMore"]')

for auto in autos:
    precio = auto.find_element(by=By.XPATH, value='.//span[@data-aut-id="itemTitle"]').text
    print(precio)

    descripcion = auto.find_element(by=By.XPATH, value='.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)
