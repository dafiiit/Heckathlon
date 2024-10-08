import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse


def download_images(url):
    # Zerlege die URL und extrahiere das letzte Segment
    folder_name = os.path.basename(urlparse(url).path)

    # Erstelle den kompletten Pfad für den Ordner (Datascraping/Data/ + letzter Bestandteil der URL)
    save_path = os.path.join("Datascraping", "Data", folder_name)

    # Erstelle den Ordner, falls er nicht existiert
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Lade die Webseite herunter
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Finde alle Bilder auf der Hauptseite
    img_tags = soup.find_all("img")

    for img in img_tags:
        img_url = img.get("src")

        # Mache die URL absolut
        img_url = urljoin(url, img_url)

        # Lade das Bild herunter
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(save_path, os.path.basename(img_url))

            # Speichere das Bild
            with open(img_name, "wb") as img_file:
                img_file.write(img_data)

            print(f"Bild heruntergeladen: {img_name}")

        except Exception as e:
            print(f"Fehler beim Herunterladen von {img_url}: {e}")


# Beispielaufruf
download_images(
    "https://www.bosch-home.com/de/de/product/geschirrspueler/geschirrspueler-freistehend/geschirrspueler-60-cm-freistehend/SMS6TCI00E"
)
