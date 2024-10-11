import time
import logging

# importieren der Klassen
from detection import ObjectDetector
from robotarm import Robotarm
from conveyorbelt import ConveyorBeltControl
from schranke import Schranke
from api_usage import API
import requests
url = 'http://localhost:3000/api/identifications'


# erstellen der Objekte
robotarm = Robotarm()
object_detector = ObjectDetector()
conveyor_control = ConveyorBeltControl()
schranke = Schranke()

logging.basicConfig(level=logging.INFO)
state = 1
blockcounter = 1  # gibt an wie viele Blöcke schon aufgehoben wurden
try: 
    while True:
        if state == 1:
            logging.info("Roboter hebt nten Block auf")
            try:
                conveyor_control.control_stopper(5, "hoch")
                while(not conveyor_control.get_conveyor_detection(5)):
                    conveyor_control.control_belt(5, "vor")
                    conveyor_control.control_belt(6, "vor")
                conveyor_control.control_belt(5, "stopp")
                conveyor_control.control_belt(6, "stopp")
                if robotarm.pick_up_block_n(blockcounter) == 42:
                    logging.info("picked up all blocks")
                    break
            except Exception as e:
                logging.error(f"Error picking up block: {str(e)}")
                # Implement appropriate error handling here
            blockcounter += 1
            state = 2
        elif state == 2:
            print("Fließbänder befödern den Block zur Kamera ")
            conveyor_control.control_belt(5, "vor")
            conveyor_control.control_belt(6, "vor")
            
            conveyor_control.control_stopper(5, "runter")
            time.sleep(1.5)
            while(not conveyor_control.get_conveyor_detection(5)):
                print("waiting to get next block")
                continue
            conveyor_control.control_belt(6, "stopp")

            conveyor_control.control_stopper(5, "hoch")
            conveyor_control.control_belt(4, "vor")
            conveyor_control.control_stopper(4, "hoch")
            
            while (not conveyor_control.get_conveyor_detection(4)):
                continue
            conveyor_control.control_belt(4, "stopp")
            conveyor_control.control_belt(5, "stopp")
            state = 3
        elif state == 3:
            print("erkenne refrigerator/oven")
            headers = {'Content-Type': 'application/json'}
            data = {
                "SerialNumber": "SN12343",
                "ApplianceType": "Coffee Machine",
                "Timestamp": 1728495446
            }

            response = requests.post(url, headers=headers, json=data)
            # refrigerator_detected, oven_detected = (
            #    object_detector.detect_oven_refrigerator()
            #)
            #print("lade die erkannten daten per API hoch")
            ##API.send_detection(refrigerator_detected, oven_detected)
            #if oven_detected:
            #    state = 4
            #elif refrigerator_detected:
            #    state = 5
            #else:
            #    print("detected nothing, trying again")
            #    state = 3
           
            if blockcounter == 2:
                state = 4
            else:
                state = 5
        elif state == 4:
            print("schließe die Schranke")
            schranke.schließe_schranke()
            state = 5
        elif state == 5:
            print("betreibe die Fließbänder nach der Kamera")
            conveyor_control.control_stopper(4, "runter")
            conveyor_control.control_belt(4, "vor")
            conveyor_control.control_stopper(3, "runter")
            conveyor_control.control_belt(3, "vor")
            conveyor_control.control_stopper(2, "runter")
            conveyor_control.control_belt(2, "vor")
            time.sleep(10)
            conveyor_control.control_belt(4, "stopp")
            conveyor_control.control_belt(3, "stopp")
            conveyor_control.control_belt(2, "stopp")
            state = 6
        elif state == 6:
            print("öffne die Schranke")
            if schranke.öffne_schranke():
                state = 1
        else:
            print("Ungültiger Wert")
except KeyboardInterrupt:
    logging.info("Program terminated by user")
except Exception as e:
    logging.error(f"Unexpected error: {str(e)}")
finally:
    # Cleanup code (e.g., stopping conveyor belts, resetting robot arm)
    logging.info("Cleaning up and exiting")
