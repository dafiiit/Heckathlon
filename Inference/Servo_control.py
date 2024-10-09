import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # GPIO 18 (Pin 12) is used for PWM

# Set PWM signal at 50Hz (a common frequency for servos)
pwm = GPIO.PWM(18, 50)  # GPIO pin 18 with 50Hz
pwm.start(0)  # Start PWM with 0% duty cycle (off)

try:
    while True:
        # Rotate the servo to 0 degrees (duty cycle: 2.5%)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)

        # Rotate the servo to 90 degrees (duty cycle: 7.5%)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)

        # Rotate the servo to 180 degrees (duty cycle: 12.5%)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    # Stop the PWM on keyboard interrupt (Ctrl + C)
    pwm.stop()
    GPIO.cleanup()