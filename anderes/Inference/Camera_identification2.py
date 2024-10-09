import cv2
import os
import time
from ultralytics import YOLO
import RPi.GPIO as GPIO

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Set up the GPIO pin for the servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # GPIO 18 (Pin 12) is used for PWM

# Set PWM signal at 50Hz (common frequency for servos)
pwm = GPIO.PWM(14, 50)  # GPIO pin 18 with 50Hz
pwm.start(0)  # Start PWM with 0% duty cycle (off)

# Define duty cycle for 45 degrees (adjust based on your servo motor)
duty_cycle_45 = 5 # 45 degrees, adjust this value if necessary

# Temporary file for the image
temp_image_path = "/tmp/captured_image.jpg"

try:
    # Capture an image using rpicam-still
    os.system(f'rpicam-still -o {temp_image_path} -t 100')  

    # Load the captured image
    frame = cv2.imread(temp_image_path)
    if frame is None:
        print("Error reading the frame.")
    else:
        frame = cv2.rotate(frame, cv2.ROTATE_180)

        # Perform object detection
        results = model(frame)

        # Check if a person is detected
        detected_person = False
        for result in results[0].boxes:
            if result.cls == 0:  # '0' is typically the class for 'person' in YOLO models
                detected_person = True
                break

        if detected_person:
            print("Person detected, rotating the motor to 45 degrees.")
            pwm.ChangeDutyCycle(5)  # Rotate the servo to 45 degrees
            time.sleep(2)  # Allow the servo to move
        else:
            print("No person detected, motor remains idle.")
            pwm.ChangeDutyCycle(2.5)  # Turn off the PWM to stop any movement
            time.sleep(2)
        # Annotate the frame with detection results and display it
        annotated_frame = results[0].plot()

except KeyboardInterrupt:
    print("Interrupted by the user.")

finally:
    # Clean up the GPIO and close the windows
    pwm.stop()
    GPIO.cleanup()
    cv2.destroyAllWindows()