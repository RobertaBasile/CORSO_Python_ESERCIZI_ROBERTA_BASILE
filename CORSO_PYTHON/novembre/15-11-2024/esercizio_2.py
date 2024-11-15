from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def basic_navigation_python_org():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    print(f"Title of the page: {driver.title}")
    
    # Trova il campo di ricerca utilizzando By.XPATH e inserisci "Python (programming language)"
    search_box = driver.find_element(By.XPATH, "//input[@id='id-search-field']")
    search_box.send_keys("Python (programming language)")
    search_box.send_keys(Keys.RETURN)
    
    # Attendi che la pagina dei risultati si carichi
    time.sleep(5)
    
    # Trova e clicca sul link "About" utilizzando By.XPATH
    about_link = driver.find_element(By.XPATH, "//a[contains(text(),'About')]")
    about_link.click()
    
    # Attendi che la pagina "About" si carichi
    time.sleep(5)
    
    # Stampa il titolo della pagina "About"
    print(f"Title of the About page: {driver.title}")
    
    time.sleep(5)
    # Chiudi il browser
    driver.quit()

# Esegui la funzione
basic_navigation_python_org()
