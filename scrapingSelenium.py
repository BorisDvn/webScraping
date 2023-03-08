from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# Firefox-Sitzung erstellen
driver = webdriver.Firefox()
driver.implicitly_wait(12)
driver.maximize_window()

# Webanwendung aufrufen
driver.get("https://www.python.org")
# Textbox lokalisieren
driver.implicitly_wait(30)
search_field = driver.find_element(By.NAME, "q")
search_field.clear()

# Suchbegriff eingeben und bestätigen
search_field.send_keys("python")
search_field.submit()
#search_bar.send_keys(Keys.RETURN)

# Liste der Suchergebnisse abrufen, die infolge der Suche angezeigt werden
# unter Zuhilfenahme der Methode find_elements_by_class_name
lists = driver.find_element(By.CLASS_NAME, "list-recent-events")

print(lists.text)

# Alle Elemente durchlaufen und individuellen Text wiedergeben
#i = 0
#for listitem in lists:
#    print(listitem.get_attribute("innerHTML"))
#    i = i + 1
#    if (i > 10):
#        break

# Browserfenster schließen
driver.quit()
