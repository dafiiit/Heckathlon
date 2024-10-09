import time
from picamera import PiCamera
from ultralytics import YOLO
import cv2

model = YOLO("yolov11n.pt")  

# Initialisiere Pi-Kamera
camera = PiCamera()
camera.resolution = (640, 480)

# Bild aufnehmen und analysieren
def capture_and_detect():
    # Bild aufnehmen
    image_path = '/home/pi/captured_image.jpg'
    camera.capture(image_path)
    print(f"Bild aufgenommen: {image_path}")

    # Bild analysieren mit YOLOv8
    results = model(image_path)

    # Ergebnisse speichern und laden
    results.save("detections")  # Speichert die Ergebnisse
    annotated_image = cv2.imread(f"detections/{image_path.split('/')[-1]}")  # Annotiertes Bild laden

    # Bild anzeigen
    cv2.imshow("YOLOv8 Detection", annotated_image)

    # Warten, bis ein Tastendruck erfolgt
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Hauptschleife zum periodischen Aufnehmen von Bildern
try:
    while True:
        capture_and_detect()
        time.sleep(5)  # Wartezeit zwischen Aufnahmen (5 Sekunden)
except KeyboardInterrupt:
    print("Programm beendet.")
finally:
    camera.close()
