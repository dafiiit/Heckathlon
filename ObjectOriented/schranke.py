import RPi.GPIO as GPIO
import time

class Schranke:
    def __init__(self, servo_pin=14):
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        
        # Set up PWM for the servo
        self.servo = GPIO.PWM(self.servo_pin, 50)  # 50Hz for servos
        self.servo.start(0)
    
    def set_angle(self, angle):
        duty = (angle / 18) + 2  # Convert angle to duty cycle
        GPIO.output(self.servo_pin, True)
        self.servo.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.servo_pin, False)
        self.servo.ChangeDutyCycle(0)
    
    def schließe_schranke(self):
        self.set_angle(45)
        wait(2000)
        return True
    
    def öffne_schranke(self):
        self.set_angle(0)
        wait(2000)
        return True
    
    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
        
if __name__ == "__main__":
    schranke = Schranke()
    schranke.schließe_schranke()
    wait(5000)
    schranke.öffne_schranke()
