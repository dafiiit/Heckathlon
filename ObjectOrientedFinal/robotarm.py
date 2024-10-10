import serial
import time

class Robotarm:
    def __init__(self, port: str = '/dev/cu.usbmodem21401', baudrate: int = 115200, timeout: int = 1):
        self.ser = serial.Serial('/dev/ttyACM0', baudrate, timeout=timeout)
        time.sleep(2)  # Geben Sie Zeit zum Herstellen der Verbindung
    
    def pick_up_block_n(self, block_n):
        if block_n == 1:
            self.pick_up_top_block()
        elif block_n == 2:
            self.pick_up_lower_block()
        elif block_n == 3:
            self.pick_up_third_block()
        else:
            return 42

    def pick_up_first_block(self):
        self.moveTo(150, 0, 150)
        self.moveToX(160)
        self.moveToY(-60)
        self.moveTo(160, -60, 60)
        self.activateSuction()
        self.moveToZ(150)
        self.moveTo(110, 150, 150)
        self.moveTo(110, 150, 80)
        self.disableSuction()
        self.moveToZ(150)
        self.moveTo(150, 0, 150)

        time.sleep(5)
        self.close()
        
    def pick_up_second_block(self):
        print("still to do")
        
        time.sleep(5)
        self.close()

    def pick_up_third_block(self):
        print("still to do")
        
        time.sleep(5)
        self.close()
    
    def moveTo(self, x: int, y: int, z: int):
        message = f"G0 X{x} Y{y} Z{z} F1000000\n"
        time.sleep(1)
        self.ser.write(message.encode('utf-8'))
        time.sleep(1)

    def moveToX(self, x: int):
        message = f"G0 X{x} F1000000\n"
        time.sleep(0.5)
        self.ser.write(message.encode('utf-8'))
        time.sleep(0.5)

    def moveToY(self, y: int):
        message = f"G0 Y{y} F1000000\n"
        time.sleep(0.5)
        self.ser.write(message.encode('utf-8'))
        time.sleep(0.5)

    def moveToZ(self, z: int):
        message = f"G0 Z{z} F1000000\n"
        time.sleep(0.5)
        self.ser.write(message.encode('utf-8'))
        time.sleep(0.5)

    def activateSuction(self):
        message = "M2231 V1\n"
        time.sleep(0.5)
        self.ser.write(message.encode('utf-8'))
        time.sleep(0.5)
        print(f"Sent: {message}")

    def disableSuction(self):
        message = "M2231 V0\n"
        time.sleep(0.5)
        self.ser.write(message.encode('utf-8'))
        time.sleep(0.5)
        print(f"Sent: {message}")

    def close(self):
        self.ser.close()
        print("Serial port is closed")

    def moveToDropZone(self):
        self.moveToZ(150)
        self.moveToY(100)
        self.moveToX(90)
        self.moveToZ(80)
        self.disableSuction()

    def returnToOrigin(self):
        self.moveTo(150, 0, 150)

    def pick_up_top_block(self):
        #Grab block
        self.moveToZ(150)
        self.returnToOrigin()
        self.moveTo(150, 0, 150)
        self.moveToX(230)
        self.moveToY(-50)
        self.moveToZ(110)
        self.activateSuction()

        #Move and drop on drop zone
        self.moveToDropZone()

        #Return to origin
        self.moveToZ(150)
        self.returnToOrigin()

    def pick_up_lower_block(self):
        #Grab block
        self.moveToZ(150)
        self.returnToOrigin()
        self.moveToX(230)
        self.moveToY(-50)
        self.moveToZ(50)
        self.activateSuction()

        #move and drop on drop zone
        self.moveToDropZone()

        #Return to origin
        self.moveToZ(150)
        self.returnToOrigin()

    #top block above: X230 Y-50 Z150
    #top block on: X230 Y-50 Z115

    #lower block above: X230 Y-50 Z150
    #lower block on: X230 Y-50 Z55

    #left lower block above: X240 Y35 Z150
    #left lower block on: X240 Y35 Z55

    def pick_up_third_block(self):
        self.moveToZ(150)
        self.returnToOrigin()
        self.moveToX(240)
        self.moveToY(35)
        self.moveToZ(50)
        self.activateSuction()

        self.moveToDropZone()

        self.moveToZ(150)
        self.returnToOrigin()

if __name__ == "__main__":
    robotarm = Robotarm()
    robotarm.pick_up_third_block()
