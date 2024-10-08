from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import requests
from ultralytics import YOLO
from PIL import Image
import io

# Lade den ChromeDriver (du musst den Pfad zu deinem WebDriver anpassen)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Im Hintergrund ausführen
service = Service("Pfad/zu/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL zur Geschirrspüler-Kategorie
category_url = "https://www.bosch-home.com/de/de/category/geschirrspueler"

def get_all_dishwasher_links(category_url):
    """Scrapt die Produktübersichtsseite und gibt Links zu allen Geschirrspülern zurück."""
    driver.get(category_url)

    # Warten, bis der "Mehr laden"-Button sichtbar und klickbar ist
    while True:
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "load-more-button"))
            )
            load_more_button.click()  # Klicke auf den Button
        except:
            print("Kein weiterer 'Mehr laden'-Button gefunden oder Fehler.")
            break

    # Den endgültigen Seiteninhalt nach dem vollständigen Laden analysieren
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Sucht alle Links, die zu den Produkten führen (Anpassung an Bosch HTML-Struktur)
    product_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        if "product/geschirrspueler" in href:  # Filtere nach Links zu Geschirrspülern
            full_url = urljoin(category_url, href)
            product_links.append(full_url)
            print(f"Gefundener Geschirrspüler-Link: {full_url}")
    
    return product_links

def download_images(url, model):
    """Lädt Bilder von einer Produktseite herunter und prüft auf bestimmte Objekte."""
    folder_name = os.path.basename(urlparse(url).path)
    save_path = os.path.join("Datascraping", "Data", folder_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    img_tags = soup.find_all("img")

    for img in img_tags:
        img_url = img.get("src")
        img_url = urljoin(url, img_url)

        if img_url.endswith('.svg'):
            print(f"SVG-Datei übersprungen: {img_url}")
            continue

        try:
            img_data = requests.get(img_url).content
            img = Image.open(io.BytesIO(img_data))

            # Run YOLO inference on the image
            results = model(img)

            # Check if "refrigerator" or "oven" is detected
            detected_objects = [model.names[int(box.cls)] for box in results[0].boxes]
            if "refrigerator" in detected_objects or "oven" in detected_objects:
                img_name = os.path.join(save_path, os.path.basename(img_url))

                with open(img_name, "wb") as img_file:
                    img_file.write(img_data)

                print(f"Bild erkannt und heruntergeladen: {img_name}")
            else:
                print(f"Kein Kühlschrank oder Ofen erkannt in: {img_url}")

        except Exception as e:
            print(f"Fehler beim Verarbeiten von {img_url}: {e}")

# Lade das YOLO-Modell
model = YOLO("yolo11n.pt")

# Hole alle Links zu den Geschirrspülern
dishwasher_links = get_all_dishwasher_links(category_url)

print(f"Insgesamt gefundene Links: {len(dishwasher_links)}")

# Lade Bilder von allen gescrapten Links herunter
for link in dishwasher_links:
    download_images(link, model)

# Schließe den Browser
driver.quit()