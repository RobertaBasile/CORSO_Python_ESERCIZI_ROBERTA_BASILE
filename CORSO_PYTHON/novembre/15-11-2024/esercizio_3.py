# andate a questo link e prendete "student" e "Password123", inseritele nel login e cliccate su submit, 
# arrivati nella pagina di accesso vi prendete il testo e lo stampate 
# e poi cliccate su log out, successivamente stampate 
# il driver.title e chiudete il driver
#https://practicetestautomation.com/practice-test-login/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_logout():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Inserisci username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    
    # Inserisci password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    
    # Clicca su submit
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    # Attendi che la pagina di accesso si carichi
    time.sleep(5)
    
    # Prendi il testo della pagina di accesso e stampalo
    success_message = driver.find_element(By.XPATH, "//div[@id='loop-container']//h1")
    print(f"Accesso riuscito: {success_message.text}")
    
    # Clicca su log out
    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    logout_button.click()
    
    # Attendi che la pagina di logout si carichi
    time.sleep(5)
    
    # Stampa il titolo della pagina
    print(f"Title of the page after logout: {driver.title}")
    
    # Chiudi il driver
    driver.quit()

# Esegui la funzione
test_login_logout()
