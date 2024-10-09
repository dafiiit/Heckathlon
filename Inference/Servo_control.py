import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # GPIO 14 (Pin 8) is used for PWM

# Set PWM signal at 50Hz (a common frequency for servos)
pwm = GPIO.PWM(14, 50)  # GPIO pin 14 with 50Hz
pwm.start(0)  # Start PWM with 0% duty cycle (off)

try:
    while True:
        # Rotate the servo to 0 degrees (duty cycle: 2.5%)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(5)

        # Rotate the servo to 90 degrees (duty cycle: 7.5%)
        pwm.ChangeDutyCycle(5)
        time.sleep(5)

except KeyboardInterrupt:
    # Stop the PWM on keyboard interrupt (Ctrl + C)
    pwm.stop()
    GPIO.cleanup()