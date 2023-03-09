from selenium import webdriver
from selenium.webdriver.common.By import By 
from selenium.webdriver.common.keys import Keys
import time

# Acessando Chromedriver
browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

# Acessando a pagina do Linkedin
browser.get("https://www.login.com/login")

# Acessando login
inpt_login = browser.find_element(By.XPATH,"")
inpt_login.send_keys("prof.gabrielsantana@gmail.com")

# Acessando senha
inpt_senha = browser.find_element(By.XPATH, "")
inpt_login.send_keys("")

# Acessando botão de login
btn_acesso = browser.find_element(By.XPATH, "")
btn_acesso.click()
