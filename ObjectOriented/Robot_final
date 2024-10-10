import serial
import time

def enable():
    message = "G92 X0 Y0 Z0"
    time.sleep(1)
    ser.write(message.encode('utf-8'))

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
    time.sleep(0.5)

def moveToY(y: int):
    message = f"G0 Y{y} F1000000\n"
    # print(message)
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))
    time.sleep(0.5)

def moveToZ(z: int):
    message = f"G0 Z{z} F1000000\n"
    # print(message)
    time.sleep(0.5)
    ser.write(message.encode('utf-8'))
    time.sleep(0.5)

def activateSuction():
    message = "M2231 V1\n"
    time.sleep(1)
    ser.write(message.encode('utf-8'))
    time.sleep(0.5)
    print(f"Sent: {message}")

def disableSuction():
    message = "M2231 V0\n"
    time.sleep(1)
    ser.write(message.encode('utf-8'))
    time.sleep(1)
    print(f"Sent: {message}")

def rotateServo(deg: int):
    message = f"M2400 S{deg}\n"
    time.sleep(1)
    ser.write(message.encode('utf-8'))
    time.sleep(1)
    print(f"Sent: {message}")

# Replace 'COM3' with your port (e.g., '/dev/ttyUSB0' for Linux)
ser = serial.Serial(
    '/dev/cu.usbmodem13301',
    baudrate=115200,
    timeout=1
)

time.sleep(2)  # Give time for the connection to establish

# if ser.isOpen():
#     print("Serial port is open")

def moveToDropZone():
    moveToZ(150)
    moveToY(100)
    moveToX(90)
    moveToZ(80)
    disableSuction()

def returnToOrigin():
    moveTo(150, 0, 150)

def pick_up_top_block():
    #Grab block
    moveToZ(150)
    returnToOrigin()
    moveTo(150, 0, 150)
    moveToX(230)
    moveToY(-50)
    moveToZ(110)
    activateSuction()

    #Move and drop on drop zone
    moveToDropZone()

    #Return to origin
    moveToZ(150)
    returnToOrigin()

def pick_up_lower_block():
    #Grab block
    moveToZ(150)
    returnToOrigin()
    moveToX(230)
    moveToY(-50)
    moveToZ(50)
    activateSuction()

    #move and drop on drop zone
    moveToDropZone()

    #Return to origin
    moveToZ(150)
    returnToOrigin()

#top block above: X230 Y-50 Z150
#top block on: X230 Y-50 Z115

#lower block above: X230 Y-50 Z150
#lower block on: X230 Y-50 Z55

#left lower block above: X240 Y35 Z150
#left lower block on: X240 Y35 Z55

def pick_up_third_block():
    moveToZ(150)
    returnToOrigin()
    moveToX(240)
    moveToY(35)
    moveToZ(50)
    activateSuction()

    moveToDropZone()

    moveToZ(150)
    returnToOrigin()

pick_up_top_block()
pick_up_lower_block()
# pick_up_third_block()
