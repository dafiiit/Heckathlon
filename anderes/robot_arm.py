import serial
import time

def moveTo(x: int, y: int, z: int):
    message = f"G0 X{x} Y{y} Z{z} F1000000\n"
    # print(message)
    time.sleep(1)
    ser.write(message.encode('utf-8'))
    time.sleep(1)

def moveToX(x: int):
    message = f"G0 X{x} F1000000\n"
    # print(message)
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))

def moveToY(y: int):
    message = f"G0 Y{y} F1000000\n"
    # print(message)
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))

def moveToZ(z: int):
    message = f"G0 Z{z} F1000000\n"
    # print(message)
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))

def activateSuction():
    message = "M2231 V1\n"
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))
    time.sleep(0.5)
    print(f"Sent: {message}")

def disableSuction():
    message = "M2231 V0\n"
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))
    time.sleep(0.5)
    print(f"Sent: {message}")

# Replace 'COM3' with your port (e.g., '/dev/ttyUSB0' for Linux)
ser = serial.Serial('/dev/ttyACM0', baudrate, timeout=timeout)


time.sleep(2)  # Give time for the connection to establish

# if ser.isOpen():
#     print("Serial port is open")

try:
    # Send data
    moveTo(150, 0, 150)
    moveToX(160)
    moveToY(-60)
    moveTo(160, -60, 60)
    activateSuction()
    moveToZ(150)
    moveTo(110, 150, 150)
    moveTo(110, 150, 80)
    disableSuction()
    moveToZ(150)
    moveTo(150, 0, 150)

    # Read response (if applicable)
    # response = ser.readline().decode('utf-8').strip()
    # if response:
    #     print(f"Received: {response}")

    time.sleep(5)

finally:
    pass
#     ser.close()
#     print("Serial port is closed")
