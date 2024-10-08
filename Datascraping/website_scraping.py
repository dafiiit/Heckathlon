import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_images(url):
    # Erstelle den Ordner für die Bilder, falls dieser nicht existiert
    if not os.path.exists('images'):
        os.makedirs('Datascraping/images')

    # Lade die Webseite herunter
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finde alle Bilder auf der Hauptseite
    img_tags = soup.find_all('img')

    for img in img_tags:
        img_url = img.get('src')

        # Mache die URL absolut
        img_url = urljoin(url, img_url)

        # Lade das Bild herunter
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join('Datascraping/images', os.path.basename(img_url))

            # Speichere das Bild
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)

            print(f'Bild heruntergeladen: {img_name}')

        except Exception as e:
            print(f'Fehler beim Herunterladen von {img_url}: {e}')

# Beispielaufruf
download_images('https://www.bosch-home.com/de/de/product/geschirrspueler/geschirrspueler-freistehend/geschirrspueler-60-cm-freistehend/SMS6TCI00E')
