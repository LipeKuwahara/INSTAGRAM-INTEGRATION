from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Configurar o driver
driver = webdriver.Chrome()

try:
    # Acessar o Instagram
    driver.get("https://www.instagram.com")
    time.sleep(5)

    # Localizar e fazer login (substitua por suas credenciais)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("USUÁRIO")
    password.send_keys("SENHA")
    password.send_keys(Keys.RETURN)
    time.sleep(10)

    # Navegar até uma postagem com enquete
    driver.get("URL_DA_ENQUETE")
    time.sleep(5)

    # Simular a votação
    # Localize os botões da votação (os seletores variam)
    options = driver.find_elements(By.CLASS_NAME, "classe_do_botão")
    if options:
        options[0].click()  # Exemplo: Clicar na primeira opção
        time.sleep(2)

finally:
    driver.quit()
