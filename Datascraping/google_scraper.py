# funktioniert so noch nicht
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Funktion zum Herunterladen eines Bildes
def download_image(url, folder_path, img_num):
    try:
        img_data = requests.get(url).content
        with open(os.path.join(folder_path, f'img_{img_num}.jpg'), 'wb') as img_file:
            img_file.write(img_data)
    except Exception as e:
        print(f"Could not download {url}. Error: {str(e)}")

# Hauptfunktion zum Scrapen von K Bildern von Google
def scrape_images(query, num_images, folder_path='data'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Setup für Selenium
    driver = webdriver.Chrome()
    driver.get('https://images.google.com')

    try:
        # Warten, bis die Suchleiste sichtbar ist
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        
        # Suchbegriff eingeben
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Seite scrollen, um mehr Bilder zu laden
        time.sleep(2)
        for _ in range(num_images // 20 + 1):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(2)

        # Seite parsen
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    finally:
        driver.quit()

    # Bilder finden
    img_tags = soup.find_all('img', {'class': 'rg_i'})

    # Bilder herunterladen
    count = 0
    for img_tag in img_tags:
        if count >= num_images:
            break
        try:
            img_url = img_tag['src'] if 'src' in img_tag.attrs else img_tag['data-src']
            if img_url.startswith('http'):
                download_image(img_url, folder_path, count)
                count += 1
        except KeyError:
            continue

    print(f"Downloaded {count} images.")

# Beispielaufruf
if __name__ == '__main__':
    query = 'landscape scenery'  # Suchbegriff
    num_images = 50  # Anzahl der herunterzuladenden Bilder
    scrape_images(query, num_images)
