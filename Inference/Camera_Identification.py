import cv2
import os
import time
from ultralytics import YOLO
import RPi.GPIO as GPIO

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # GPIO 14 (Pin 8) is used for PWM

# Set PWM signal at 50Hz (a common frequency for servos)
pwm = GPIO.PWM(14, 50)  # GPIO pin 14 with 50Hz
pwm.start(0)  # Start PWM with 0% duty cycle (off)

# Lade das YOLOv11 Modell
model = YOLO("yolo11n.pt")

# Temporäre Datei für das Bild
temp_image_path = "/tmp/captured_image.jpg"
n = 0
while True:

    pwm.ChangeDutyCycle(2.5)

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

    # Zeige die Ergebnisse anqqq
    cv2.imshow('YOLOv11', annotated_frame)
    if not results:
        detected_person = False
    else:
        detected_person = any(
            (result.boxes.cls.numel() > 0 and (result.boxes.cls == 0).any()) 
            for result in results
        )
        
    if detected_person:
        target_duty_cycle = 5
    else:
        target_duty_cycle = 2.5

    if abs(last_duty_cycle - target_duty_cycle) > 0.1:  # Nur ändern, wenn der Unterschied signifikant ist
        pwm.ChangeDutyCycle(target_duty_cycle)
        last_duty_cycle = target_duty_cycle
        time.sleep(0.1)  # Warte 100 ms


    # Beende die Schleife, wenn die Taste 'q' gedrückt wird
    if cv2.waitKey(1) == ord('q'):
        break

# Fenster schließen
cv2.destroyAllWindows()
