import cv2
import os
import random
import time
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        # Lade das YOLO-Modell
        self.model = YOLO("yolo11n.pt")
        self.temp_image_path = "/tmp/captured_image.jpg"
        self.fridge_folder = "refrigerator_data"
        self.oven_folder = "oven_data"
        self.train_folder = "train_data"
        self.val_folder = "val_data"
        self.create_folders()

    def create_folders(self):
        # Erstelle Ordner für Trainings- und Validierungsdaten
        os.makedirs(self.fridge_folder, exist_ok=True)
        os.makedirs(self.oven_folder, exist_ok=True)
        os.makedirs(self.train_folder, exist_ok=True)
        os.makedirs(self.val_folder, exist_ok=True)

    def capture_image(self):
        # Nimm ein Foto mit rpicam-still auf
        os.system(f'rpicam-still -o {self.temp_image_path} -t 1')  # 1 Sekunde für die Kameraumstellung
        return self.temp_image_path

    def detect(self):
        # Lade das Bild und wende YOLO-Modell darauf an
        image_path = self.capture_image()
        results = self.model(image_path)  # YOLO auf das Bild anwenden
        return results

    def detect_oven_refrigerator(self):
        # Verwende die detect-Methode, um Objekte zu erkennen
        results = self.detect()

        # Initialisiere Variablen für die Ausgabe
        oven_detected = False
        refrigerator_detected = False

        # Gehe durch die Ergebnisse und suche nach Ofen und Kühlschrank
        for result in results:
            # Access the predicted boxes and corresponding classes
            for box in result.boxes:  # Each `box` is an object prediction
                class_id = int(box.cls[0])  # Access the class ID
                
                # Check for refrigerator or oven class based on your trained model IDs
                if class_id == 0:  # Assuming class ID 0 is for 'refrigerator'
                    refrigerator_detected = True
                elif class_id == 1:  # Assuming class ID 1 is for 'oven'
                    oven_detected = True

        return oven_detected, refrigerator_detected

    def preview(self):
        # Vorschau des aufgenommenen Bildes
        img = cv2.imread(self.temp_image_path)
        cv2.imshow("Captured Image", img)
        cv2.waitKey(3000)  # Bild für 3 Sekunden anzeigen
        cv2.destroyAllWindows()


# Wird ausgeführt wenn dieses Programm direkt ausgeführt wird
if __name__ == "__main__":
    # Objekt der Klasse erstellen und die detect Methode ausführen
    detector = ObjectDetector()
    oven, refrigerator = detector.detect_oven_refrigerator()
    print("Oven: ", oven)
    print("Refrigerator: ", refrigerator)
    detector.preview()