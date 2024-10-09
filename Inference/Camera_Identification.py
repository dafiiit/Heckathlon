import cv2
import os
import time
from ultralytics import YOLO

# Lade das YOLOv11 Modell
model = YOLO("yolo11n.pt")

# Temporäre Datei für das Bild
temp_image_path = "/tmp/captured_image.jpg"

while True:
    # Nimm ein Foto mit rpicam-still auf
    os.system(f'rpicam-still -o {temp_image_path} -t 100')  

    # Lade das Bild
    frame = cv2.imread(temp_image_path)
    if frame is None:
        print("Fehler beim Lesen des Frames.")
        break

    frame = cv2.rotate(frame, cv2.ROTATE_180)

    # Führe die Objekterkennung durch
    results = model(frame)

    # Ergebnisse rendern
    annotated_frame = results[0].plot()

    # Zeige die Ergebnisse an
    cv2.imshow('YOLOv11', annotated_frame)

    # Beende die Schleife, wenn die Taste 'q' gedrückt wird
    if cv2.waitKey(1) == ord('q'):
        break

# Fenster schließen
cv2.destroyAllWindows()
