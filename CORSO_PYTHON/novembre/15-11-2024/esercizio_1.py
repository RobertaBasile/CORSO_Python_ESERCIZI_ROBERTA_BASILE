from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

# driver = webdriver.Chrome()

# driver.get("https://www.python.org")

# search_bar = driver.find_element(By.XPATH, "q")

# driver.quit()

# search_bar.send_keys("selenium")

# Visita Wikipedia, 
# cerca "Python (programming language)", 
# e stampa il titolo della pagina dei risultati

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def basic_navigation_wikipedia():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    print(f"Title of the page: {driver.title}")
    
    # Trova il campo di ricerca e inserisci "Python (programming language)"
    # Trova il campo di ricerca utilizzando By.XPATH e inserisci "Python (programming language)" 
    # [@name='search']: Filtra gli elementi <input> per quelli che hanno un attributo name con il valore search.
    search_box = driver.find_element(By.XPATH, "//input[@name='search']")
    # search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Python (programming language)")
    search_box.send_keys(Keys.RETURN)
    
    # Attendi che la pagina dei risultati si carichi
    time.sleep(5)
    
    # Stampa il titolo della pagina dei risultati
    print(f"Title of the results page: {driver.title}")
    time.sleep(3)
    
    # Chiudi il browser
    driver.quit()

# Esegui la funzione
basic_navigation_wikipedia()

    
    