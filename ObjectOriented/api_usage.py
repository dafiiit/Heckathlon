#Import some things
class API:
    def __init__(self):
        print("some initialisations")
    def send_detection(self, oven_detected, refrigerator_detected):
        if oven_detected:
            print("send oven detected")
        elif refrigerator_detected:
            print("send refrigerator detected")
        else:
            print("error")