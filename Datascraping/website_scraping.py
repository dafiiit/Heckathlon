import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
from ultralytics import YOLO
from PIL import Image
import io

def download_images(url, model):
    folder_name = os.path.basename(urlparse(url).path)
    save_path = os.path.join("Datascraping", "Data", folder_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    response = requests.get(url)
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

# Example usage
download_images(
    "https://www.bosch-home.com/de/de/product/geschirrspueler/geschirrspueler-freistehend/geschirrspueler-60-cm-freistehend/SMS6TCI00E",
    model
)