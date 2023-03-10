from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from config import login
import time

# Acessando Chromedriver
browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

# Acessando a pagina do Linkedin
browser.get("https://www.linkedin.com/login")

# Acessando login
time.sleep(3)
inpt_login = browser.find_element(By.XPATH,"//*[@id='username']")
inpt_login.send_keys(login["email"])


# Acessando senha
time.sleep(3)
inpt_senha = browser.find_element(By.XPATH, "//*[@id='password']")
inpt_senha.send_keys(login["senha"])


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
extract_nav = browser.find_element(By.XPATH, f"//*[@id='search-reusables__filters-bar']/ul").text

# Identificando a opção "Pessoas" no menu 
lista = []
contador = index = 0
palavra = ""
for item in extract_nav:    
    if item == "\n":
        contador += 1        
        if palavra == "Pessoas":
            index = contador 
            lista.append(palavra)
            palavra ='' 
        else:
            lista.append(palavra)
            palavra ='' 
    else:
        palavra += item   

# Resultado do menu
print(lista[index])   

# Acessando menu "Pessoas"
time.sleep(5)
btn_pessoas = browser.find_element(By.XPATH, f"//*[@id='search-reusables__filters-bar']/ul/li[{index}]")
btn_pessoas.click()

for _ in range(4):
    btn_pessoas.send_keys(Keys.TAB)

input("")
