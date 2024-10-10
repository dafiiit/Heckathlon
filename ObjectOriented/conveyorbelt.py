import cps_gate_python_interface as cps_interface
import cps_gate_constants as cps_constants

class ConveyorBeltControl:
    def __init__(self):
        self.cps_gates = {
            1: self._create_gate(cps_constants.cps01),
            2: self._create_gate(cps_constants.cps02),
            3: self._create_gate(cps_constants.cps03),
            4: self._create_gate(cps_constants.cps04),
            5: self._create_gate(cps_constants.cps05),
            6: self._create_gate(cps_constants.cps06)
        }

    def _create_gate(self, address):
        return cps_interface.Class_CPSGateControl(
            address,
            cps_constants.conveyorbelt_right_flag,
            cps_constants.conveyorbelt_left_flag,
            cps_constants.conveyorbelt_stop_flag,
            cps_constants.stopper_down_flag,
            cps_constants.stopper_up_flag,
            cps_constants.conveyor_detection_flag
        )

    def control_belt(self, belt_number, direction):
        if belt_number not in self.cps_gates:
            raise ValueError(f"Invalid belt number: {belt_number}. Must be between 1 and 6.")
        
        gate = self.cps_gates[belt_number]
        
        try:
            if direction == "vor":
                gate.run_conveyorbelt_right()
            elif direction == "rück":
                gate.run_conveyorbelt_left()
            elif direction == "stopp":
                gate.stop_conveyorbelt()
            else:
                raise ValueError(f"Invalid direction: {direction}. Must be 'vor', 'rück', or 'stopp'.")
        except Exception as e:
            print(f"Error controlling belt {belt_number}: {str(e)}")
            # Implement appropriate error handling or logging here

    def control_stopper(self, belt_number, position):
        if belt_number not in self.cps_gates:
            raise ValueError(f"Invalid belt number: {belt_number}. Must be between 1 and 6.")
        
        gate = self.cps_gates[belt_number]
        
        if position == "hoch":
            gate.move_stopper_up()
        elif position == "runter":
            gate.move_stopper_down()
        else:
            raise ValueError(f"Invalid position: {position}. Must be 'hoch' or 'runter'.")

    def get_conveyor_detection(self, belt_number):
        if belt_number not in self.cps_gates:
            raise ValueError(f"Invalid belt number: {belt_number}. Must be between 1 and 6.")
        
        return self.cps_gates[belt_number].conveyor_detection_state()

# Example usage:
if __name__ == "__main__":
    conveyor_control = ConveyorBeltControl()
    conveyor_control.control_belt(4, "vor")
    conveyor_control.control_stopper(4, "runter")
    if conveyor_control.get_conveyor_detection(3):
        conveyor_control.control_stopper(4, "hoch")
