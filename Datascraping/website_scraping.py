import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
from ultralytics import YOLO
from PIL import Image
import io

# User-Agent, um nicht blockiert zu werden
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_all_dishwasher_links(category_url):
    """Scrapt die Produktübersichtsseite und gibt Links zu allen Geschirrspülern zurück."""
    response = requests.get(category_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Fehler beim Laden der Seite: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
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

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Bosch Geschirrspüler-Kategorie-Seite
category_url = "https://www.bosch-home.com/de/de/category/geschirrspueler"

# Alle Links zu den Geschirrspülern auf der Seite extrahieren
dishwasher_links = get_all_dishwasher_links(category_url)

print(f"Insgesamt gefundene Links: {len(dishwasher_links)}")

# Lade Bilder von allen gescrapten Links
for link in dishwasher_links:
    download_images(link, model)
