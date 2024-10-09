import cps_gate_python_interface as cps_interface
import cps_gate_constants as cps_constants
import time

# Instantiate CPSGateControl for each CPS gate
cps_gates = {
    '1': cps_interface.Class_CPSGateControl(
        cps_constants.cps01, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

    

    '2': cps_interface.Class_CPSGateControl(
        cps_constants.cps02, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),


        '3': cps_interface.Class_CPSGateControl(
        cps_constants.cps03, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '4': cps_interface.Class_CPSGateControl(
        cps_constants.cps04, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '5': cps_interface.Class_CPSGateControl(
        cps_constants.cps05, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '6': cps_interface.Class_CPSGateControl(
        cps_constants.cps06, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),
}

# Function to run all conveyor belts right
def run_all():
    for gate in cps_gates.values():
        gate.run_conveyorbelt_right()

# Function to stop all conveyor belts
def all_stop():
    for gate in cps_gates.values():
        gate.stop_conveyorbelt()

# Function to move all stoppers down
def all_down():
    for gate in cps_gates.values():
        gate.move_stopper_down()

# Function to move all stoppers up
def all_up():
    for gate in cps_gates.values():
        gate.move_stopper_up()


while True:
    print("Available inputs:")
    print("r: Run conveyor belt right")
    print("l: Run conveyor belt left")
    print("s: Stop conveyor belt ")
    print("u: Move stopper down")
    print("p: Move stopper up")
    print("d: Check conveyor detection flag")
    print("")    
    print("special commands:")
    print("example usage: 1a -> cps01 run conveyor belt right")
    print("example usage: 6k -> cps06 check conveyor detection")
    print("run all, stop all, all down, all up")
    print("")
    # Add similar inputs for other gates...

    command = input("Enter command: ")

    if command == "#r":
        run_all()
    elif command == "#s":
        all_stop()
    elif command == "#d":
        all_down()
    elif command == "#u":
        all_up()
    else:

        if len(command) >= 2:
            gate_number = command[0]
            specific_command = command[1]

            if gate_number in cps_gates:
                gate = cps_gates[gate_number]

                if specific_command == 'r':
                    gate.run_conveyorbelt_right()
                elif specific_command == 'l':
                    gate.run_conveyorbelt_left()
                elif specific_command == 's':
                    gate.stop_conveyorbelt()
                elif specific_command == 'd':
                    gate.move_stopper_down()
                elif specific_command == 'u':
                    gate.move_stopper_up()
                elif specific_command == 'c':
                    conveyor_detection = gate.conveyor_detection_state()
                    print(f"CPS{gate_number} - Conveyor Detection Flag:", conveyor_detection)
                else:
                    print("Invalid command. Please use r, l, s, u, d, or d.")
            else:
                print(f"Gate {gate_number} doesn't exist.")
        else:
            print("Invalid command format. Use GateNumber+Command, e.g., 1j, 2k.")
    
    time.sleep(0.2)


