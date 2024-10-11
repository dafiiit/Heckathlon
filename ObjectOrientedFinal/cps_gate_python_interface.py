# this file is for interfacing with the cps gate with python
# the intferface takes away the pain to learn the IEC61131-3 langues wich are needed to get the cps gates running
# IEC61131-3 langues is the industrie standard for PLC programming

# Author Elias Fischer 11/23

#imports
from opcua import Client


class Class_CPSGateControl:
    def __init__(self, server_address, conveyorbelt_right_flag, conveyorbelt_left_flag, conveyorbelt_stop_flag, stopper_down_flag, stopper_up_flag, conveyor_detection_flag):
        try: 
            self.client = Client(server_address)
            self.client.connect()
            
            self.conveyorbelt_right = self.client.get_node(conveyorbelt_right_flag)
            self.conveyorbelt_left = self.client.get_node(conveyorbelt_left_flag)
            self.conveyorbelt_stop = self.client.get_node(conveyorbelt_stop_flag)
            self.stopper_down = self.client.get_node(stopper_down_flag)
            self.stopper_up = self.client.get_node(stopper_up_flag)
            self.conveyor_detection = self.client.get_node(conveyor_detection_flag)
        except Exception as e:
            print(f"Error connecting to CPS Gate: {str(e)}") 
            raise
    
    def run_conveyorbelt_right(self):
        try:
            self.conveyorbelt_right.set_value(True)
        except Exception as e:
            print(f"Error running conveyor belt right: {str(e)}")
    
    def run_conveyorbelt_left(self):
        try: 
            self.conveyorbelt_left.set_value(True)
        except Exception as e:
            print(f"Error running conveyor belt left: {str(e)}")
        
    def stop_conveyorbelt(self):
        try: 
            self.conveyorbelt_stop.set_value(True)
        except Exception as e:
            print(f"Error stopping conveyor belt: {str(e)}")
    
    def move_stopper_down(self):
        try: 
            self.stopper_down.set_value(True)
        except Exception as e:
            print(f"Error moving stopper down: {str(e)}")
        
    def move_stopper_up(self):
        try:
            self.stopper_up.set_value(True)
        except Exception as e:
            print(f"Error moving stopper up: {str(e)}")
    
    def conveyor_detection_state(self):
        return self.conveyor_detection.get_value()
    

