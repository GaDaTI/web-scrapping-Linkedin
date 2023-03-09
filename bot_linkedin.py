from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

# Acessando Chromedriver
browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

# Acessando a pagina do Linkedin
browser.get("https://www.linkedin.com/login")

# Acessando login
time.sleep(3)
inpt_login = browser.find_element(By.XPATH,"//*[@id='username']")
inpt_login.send_keys("prof.gabrielsantana@gmail.com")

# Acessando senha
time.sleep(3)
inpt_senha = browser.find_element(By.XPATH, "//*[@id='password']")
inpt_senha.send_keys("G@Da!978")

# Acessando botão de login
time.sleep(5)
btn_acesso = browser.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
btn_acesso.click()

# Acessando a barra de pesquisa
time.sleep(3)
inpt_pesquisa = browser.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
inpt_pesquisa.send_keys("Desenvolvedor Sênior")
time.sleep(2)
inpt_pesquisa.send_keys(Keys.RETURN)

# Acessando barra de navegação
time.sleep(5)
lista = []
for index in range(9):    
    extract_nav = browser.find_element(By.XPATH, f"/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ulli[{index}]").text
    lista_nav.append(extract_nav)


time.sleep(5)
print(lista_nav)
input("")
