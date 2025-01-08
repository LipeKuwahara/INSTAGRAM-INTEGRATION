from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Solicitar as credenciais ao usuário
username_input = input("Digite seu nome de usuário do Instagram: ")
password_input = input("Digite sua senha do Instagram: ")

# Configurar o driver
driver = webdriver.Chrome()

try:
    # Acessar o Instagram
    driver.get("https://www.instagram.com")
    time.sleep(5)

    # Localizar e fazer login usando as credenciais fornecidas
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys(username_input)
    password.send_keys(password_input)
    password.send_keys(Keys.RETURN)
    time.sleep(10)

    # Navegar até uma postagem com enquete
    driver.get("URL_ENQUETE")
    time.sleep(5)

    # Simular a votação (exemplo de interação com as opções)
    options = driver.find_elements(By.CLASS_NAME, "classe_do_botão")
    if options:
        options[0].click()  # Exemplo: Clicar na primeira opção
        time.sleep(2)

finally:
    driver.quit()