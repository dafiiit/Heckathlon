import time
from picamera import PiCamera
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov11n.pt")

# Initialisiere Pi-Kamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

# Kamera Vorschau einrichten
cv2.namedWindow("Camera Preview", cv2.WINDOW_NORMAL)

# Bild aufnehmen und analysieren
def capture_and_detect():
    # Live Bild von Kamera holen
    image = np.empty((480, 640, 3), dtype=np.uint8)
    camera.capture(image, 'bgr')
    
    # YOLO-Modell anwenden
    results = model(image)
    
    # Annotiertes Bild
    annotated_image = results.plot()  # Ergebnisse im Bild markieren
    
    # Bild in einem Fenster anzeigen
    cv2.imshow("Camera Preview", annotated_image)

# Hauptschleife für kontinuierliche Vorschau und Erkennung
try:
    while True:
        capture_and_detect()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Beendet die Schleife bei Tastendruck 'q'
except KeyboardInterrupt:
    print("Programm beendet.")
finally:
    camera.close()
    cv2.destroyAllWindows()