
from detection.py import ObjectDetector


state = 1
blockcounter = 0 #gibt an wie viele Blöcke schon aufgehoben wurden
while true:
    if state == 1:
        print("Roboter hebt nten Block auf")
        #do it here (blockcounter)
        blockcounter = blockcounter+1
        state = 2 
    elif state == 2:
        print("Fließbänder befödern den Block zur Kamera ")
        #do it here 
        state = 3
    elif state == 3:
        print("erkenne refrigerator/oven")
        print("lade die erkannten daten per API hoch")
        if oven: 
            state = 4
        else:
            state = 5
    elif state == 4:
        print("fahre die Schranke aus")
        #do it here
        state = 5
    elif state == 5:
        print("betreibe die Fließbänder nach der Kamera")
        #do it here
        state = 6
    elif state == 6:
        print("fahre die Schranke wieder ein" )
        # do it here
        state = 1
    else:
        return "Ungültiger Wert"

