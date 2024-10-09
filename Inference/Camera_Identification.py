import cv2
import torch
import time
from ultralytics import YOLO

# Lade das YOLOv11 Modell
model = YOLO("yolo11n.pt")

# Initialisiere die Kamera
cap = cv2.VideoCapture(0)

while True:
    # Lese ein Frame von der Kamera
    ret, frame = cap.read()

    # Führe die Objekterkennung durch
    results = model(frame)

    # Zeige die Ergebnisse an
    cv2.imshow('YOLOv11', results.render()[0])

    # Beende die Schleife, wenn die Taste 'q' gedrückt wird
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()